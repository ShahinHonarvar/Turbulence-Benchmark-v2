def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    sub_list = numbers[6:9]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list, reverse=True)
    return sorted_sub_list[1] if len(sorted_sub_list) > 1 else None