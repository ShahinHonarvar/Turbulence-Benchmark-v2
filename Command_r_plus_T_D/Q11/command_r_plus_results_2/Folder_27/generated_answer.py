def find_largest_num(numbers):
    if not numbers:
        return None
    start_index = 66
    end_index = 93
    if start_index >= len(numbers) or end_index >= len(numbers):
        return None
    sliced_numbers = numbers[start_index:end_index + 1]
    return max(sliced_numbers)