def find_second_smallest_num(numbers):
    if len(numbers) < 751:
        return None
    sub_list = numbers[246:751]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(set(sub_list))
    return unique_sorted[1] if len(unique_sorted) > 1 else None