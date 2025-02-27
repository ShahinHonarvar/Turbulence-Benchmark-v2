def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    sub_list = numbers[15:40]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]