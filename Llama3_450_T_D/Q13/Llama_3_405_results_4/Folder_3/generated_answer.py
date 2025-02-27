def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sliced_numbers = numbers[62:93]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[-2]