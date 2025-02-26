def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    sub_list = numbers[56:83]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(set(sub_list), reverse=True)
    return sorted_sub_list[1] if len(sorted_sub_list) >= 2 else None