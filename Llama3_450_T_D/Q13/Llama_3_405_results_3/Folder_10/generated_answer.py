def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    sliced_numbers = numbers[25:60]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[-2]