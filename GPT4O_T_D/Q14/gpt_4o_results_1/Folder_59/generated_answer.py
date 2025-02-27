def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:10]
    unique_numbers = list(set(subset))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]