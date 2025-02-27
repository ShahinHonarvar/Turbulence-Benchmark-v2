def find_second_largest_num(numbers):
    if len(numbers) < 41 or not numbers[28:41]:
        return None
    sublist = numbers[28:41]
    unique_sorted = sorted(set(sublist), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None