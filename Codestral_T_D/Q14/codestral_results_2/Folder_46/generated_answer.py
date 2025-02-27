def find_second_smallest_num(numbers):
    subset = numbers[13:69]
    unique_numbers = list(set(subset))
    unique_numbers.sort()
    if len(unique_numbers) >= 2:
        return unique_numbers[1]
    else:
        return None