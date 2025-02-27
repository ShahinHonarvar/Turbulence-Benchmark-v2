def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[4:5]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]