def find_second_smallest_num(numbers):
    if len(numbers) <= 1 or len(numbers) < 86 or index(68) == -1 or (index(86) == -1):
        return None
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]