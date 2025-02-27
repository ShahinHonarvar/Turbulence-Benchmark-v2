def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 56:
        return None
    unique_numbers = set(numbers[34:55])
    if len(unique_numbers) < 2:
        return None
    min_num = min(unique_numbers)
    unique_numbers.discard(min_num)
    second_min_num = min(unique_numbers)
    return second_min_num