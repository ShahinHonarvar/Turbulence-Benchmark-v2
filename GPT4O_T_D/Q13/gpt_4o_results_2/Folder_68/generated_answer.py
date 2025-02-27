def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[:9]) < 2:
        return None
    limited_numbers = numbers[:9]
    largest = max(limited_numbers)
    limited_numbers.remove(largest)
    second_largest = max(limited_numbers) if limited_numbers else None
    return second_largest