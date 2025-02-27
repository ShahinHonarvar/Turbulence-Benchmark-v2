def find_second_largest_num(numbers):
    sublist = numbers[10:101]
    if len(sublist) < 2:
        return None
    unique_sorted_numbers = sorted(set(sublist), reverse=True)
    return unique_sorted_numbers[1] if len(unique_sorted_numbers) >= 2 else None