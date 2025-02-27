def find_second_smallest_num(numbers):
    subset = numbers[50:55]
    unique_numbers = list(set(subset))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    else:
        return unique_numbers[1]