def find_second_smallest_num(numbers):
    sublist = numbers[6:9]
    if len(sublist) < 2:
        return None
    unique_numbers = list(sorted(set(sublist)))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]