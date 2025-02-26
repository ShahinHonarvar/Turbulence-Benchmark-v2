def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[29:52]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(set(sub_list))
    return sorted_sub_list[1] if len(sorted_sub_list) >= 2 else None