def find_second_smallest_num(numbers):
    if len(numbers) < 92:
        return None
    sub_list = numbers[91:100]
    if len(sub_list) == 0:
        return None
    sorted_sub_list = sorted(set(sub_list))
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]