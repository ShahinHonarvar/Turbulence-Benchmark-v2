def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 2:
        return None
    sub_list = numbers[1:101]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1] if len(sorted_sub_list) >= 2 else None