def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    sub_list = numbers[75:89]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[-2]