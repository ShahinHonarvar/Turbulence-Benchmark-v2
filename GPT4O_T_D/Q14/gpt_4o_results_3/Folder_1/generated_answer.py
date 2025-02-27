def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    sublist = numbers[34:56]
    if len(sublist) < 2:
        return None
    unique_sorted_numbers = sorted(set(sublist))
    if len(unique_sorted_numbers) < 2:
        return None
    return unique_sorted_numbers[1]