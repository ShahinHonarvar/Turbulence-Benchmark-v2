def find_second_largest_num(numbers):
    if len(numbers) < 41:
        return None
    sliced_numbers = numbers[28:41]
    largest = max(sliced_numbers)
    sliced_numbers = [num for num in sliced_numbers if num != largest]
    if not sliced_numbers:
        return None
    return max(sliced_numbers)