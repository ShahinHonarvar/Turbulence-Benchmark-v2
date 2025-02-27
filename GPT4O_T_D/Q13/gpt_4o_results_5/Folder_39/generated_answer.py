def find_second_largest_num(numbers):
    sub_list = numbers[20:31]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(set(sub_list), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None