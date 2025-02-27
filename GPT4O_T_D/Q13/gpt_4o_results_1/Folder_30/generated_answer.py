def find_second_largest_num(numbers):
    if len(numbers) < 99 or len(numbers) <= 55:
        return None
    sublist = numbers[55:99]
    unique_sorted = sorted(set(sublist))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[-2]