def find_second_largest_num(numbers):
    if len(numbers) <= 75:
        return None
    sub_list = numbers[75:89]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list, reverse=True)
    return sorted_sub_list[1]