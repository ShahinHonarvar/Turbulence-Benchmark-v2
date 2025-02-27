def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    sliced_numbers = numbers[12:93]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[1]