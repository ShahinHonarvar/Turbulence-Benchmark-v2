def find_second_largest_num(numbers):
    if len(numbers) < 87 or len(numbers) < 43:
        return None
    sub_list = numbers[43:87]
    if len(set(sub_list)) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]