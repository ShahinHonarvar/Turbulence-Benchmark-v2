def find_second_largest_num(numbers):
    numbers_in_range = numbers[25:53]
    unique_numbers = set(numbers_in_range)
    if len(unique_numbers) < 2:
        return None
    else:
        sorted_numbers = sorted(unique_numbers)
        return sorted_numbers[-2]