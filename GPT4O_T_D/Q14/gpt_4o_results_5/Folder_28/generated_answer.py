def find_second_smallest_num(numbers):
    if len(numbers) < 51:
        return None
    sublist = numbers[22:51]
    if len(sublist) < 2:
        return None
    unique_numbers = sorted(set(sublist))
    return unique_numbers[1] if len(unique_numbers) >= 2 else None