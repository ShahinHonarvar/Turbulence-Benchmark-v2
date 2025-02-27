def find_second_smallest_num(numbers):
    filtered_numbers = [num for num in numbers[21:98] if num is not None]
    if len(filtered_numbers) < 2:
        return None
    filtered_numbers = sorted(filtered_numbers)
    return filtered_numbers[1]