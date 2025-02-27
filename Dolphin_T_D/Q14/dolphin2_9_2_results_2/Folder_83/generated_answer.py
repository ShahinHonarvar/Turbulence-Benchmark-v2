def find_second_smallest_num(numbers):
    subset = [num for pos, num in enumerate(numbers) if 90 <= pos <= 200]
    unique_numbers = list(set(subset))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    else:
        return unique_numbers[1]