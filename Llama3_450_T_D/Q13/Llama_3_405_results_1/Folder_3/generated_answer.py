def find_second_largest_num(numbers):
    if len(numbers) < 63:
        return None
    sliced_numbers = numbers[62:93]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort(reverse=True)
    return sliced_numbers[1] if len(sliced_numbers) > 1 else None