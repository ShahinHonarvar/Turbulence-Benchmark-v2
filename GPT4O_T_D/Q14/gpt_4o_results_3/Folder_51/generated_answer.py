def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sub_list = numbers[1:9]
    unique_sorted = sorted(set(sub_list))
    return unique_sorted[1] if len(unique_sorted) > 1 else None