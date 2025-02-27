def find_second_largest_num(numbers):
    if len(numbers) < 4:
        return None
    sub_list = numbers[:4]
    unique_sorted = sorted(set(sub_list), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None