def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 60:
        return None
    sub_list = numbers[59:98]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(set(sub_list), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None