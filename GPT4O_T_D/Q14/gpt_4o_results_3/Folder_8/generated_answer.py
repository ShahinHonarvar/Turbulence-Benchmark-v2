def find_second_smallest_num(numbers):
    sub_list = numbers[56:67]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(set(sub_list))
    return unique_sorted[1] if len(unique_sorted) > 1 else None