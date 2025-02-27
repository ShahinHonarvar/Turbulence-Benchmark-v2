def find_second_largest_num(numbers):
    if len(numbers) < 56:
        return None
    sliced_numbers = numbers[27:56]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers, reverse=True)
    return sorted_numbers[1]