def find_second_smallest_num(numbers):
    if len(numbers) <= 23:
        return None
    sub_list = numbers[23:24]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1] if len(sub_list) > 1 else None