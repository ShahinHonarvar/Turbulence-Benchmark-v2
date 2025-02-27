def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[1:6]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[-2]