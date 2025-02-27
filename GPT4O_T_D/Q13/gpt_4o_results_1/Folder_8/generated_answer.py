def find_second_largest_num(numbers):
    if len(numbers) < 24:
        return None
    sublist = numbers[23:24]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]