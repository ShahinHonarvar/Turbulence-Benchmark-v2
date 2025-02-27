def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    sub_list = numbers[25:88]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]