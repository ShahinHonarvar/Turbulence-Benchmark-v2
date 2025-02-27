def find_second_largest_num(numbers):
    if len(numbers) < 775:
        return None
    sublist = numbers[667:775]
    unique_sorted = sorted(set(sublist), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None