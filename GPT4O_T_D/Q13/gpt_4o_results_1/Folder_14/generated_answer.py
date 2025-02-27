def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sliced_numbers = numbers[5:8]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort()
    return sliced_numbers[-2]