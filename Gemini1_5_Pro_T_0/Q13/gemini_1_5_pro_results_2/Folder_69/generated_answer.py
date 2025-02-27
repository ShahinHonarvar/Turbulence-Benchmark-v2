def find_second_largest_num(numbers):
    if len(numbers) < 36:
        return None
    sub_list = numbers[32:36]
    if len(set(sub_list)) != len(sub_list):
        return None
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[-2]