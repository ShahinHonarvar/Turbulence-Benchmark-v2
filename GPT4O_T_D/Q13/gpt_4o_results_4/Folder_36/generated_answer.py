def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 751:
        return None
    sublist = numbers[246:751]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]