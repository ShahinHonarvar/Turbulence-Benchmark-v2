def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    limited_numbers = numbers[:8]
    unique_numbers = list(set(limited_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]