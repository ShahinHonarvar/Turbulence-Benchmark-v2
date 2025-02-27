def find_second_smallest_num(numbers):
    sublist = numbers[75:95]
    if len(sublist) < 2:
        return None
    unique_numbers = sorted(set(sublist))
    return unique_numbers[1] if len(unique_numbers) > 1 else None