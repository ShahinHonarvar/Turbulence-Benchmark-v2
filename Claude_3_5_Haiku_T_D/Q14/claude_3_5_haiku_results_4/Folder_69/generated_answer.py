def find_second_smallest_num(numbers):
    if len(numbers) <= 26:
        return None
    sub_list = numbers[25:88]
    if len(sub_list) == 0:
        return None
    sorted_sub_list = sorted(set(sub_list))
    return sorted_sub_list[1] if len(sorted_sub_list) >= 2 else None