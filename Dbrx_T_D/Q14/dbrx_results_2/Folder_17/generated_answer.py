def find_second_smallest_num(numbers):
    numbers = [n for n in numbers[28:39] if n is not None]
    if len(numbers) < 2:
        return None
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]