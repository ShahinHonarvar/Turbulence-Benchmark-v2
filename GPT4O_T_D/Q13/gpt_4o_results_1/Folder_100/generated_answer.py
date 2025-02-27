def find_second_largest_num(numbers):
    sublist = numbers[42:69]
    if len(sublist) < 2:
        return None
    unique_numbers = sorted(set(sublist), reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]