def find_second_largest_num(numbers):
    if len(numbers) < 11 or len(numbers) > 101:
        return None
    sub_list = numbers[10:101]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[-2]