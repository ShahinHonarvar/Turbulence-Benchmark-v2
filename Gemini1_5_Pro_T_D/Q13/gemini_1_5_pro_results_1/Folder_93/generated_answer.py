def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return None
    sub_list = numbers[75:95]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]