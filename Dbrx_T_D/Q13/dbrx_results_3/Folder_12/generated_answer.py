def find_second_largest_num(numbers):
    numbers = numbers[14:65]
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[-2]