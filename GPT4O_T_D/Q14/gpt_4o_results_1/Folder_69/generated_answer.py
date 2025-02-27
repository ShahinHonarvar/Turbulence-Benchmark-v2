def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    sublist = numbers[25:88]
    if len(sublist) < 2:
        return None
    unique_numbers = sorted(set(sublist))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]