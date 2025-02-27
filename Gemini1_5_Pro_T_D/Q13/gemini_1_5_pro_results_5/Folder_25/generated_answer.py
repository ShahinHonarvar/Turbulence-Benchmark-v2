def find_second_largest_num(numbers):
    if len(numbers) < 94 or len(numbers) < 30:
        return None
    sub_list = numbers[29:94]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list))[-2]