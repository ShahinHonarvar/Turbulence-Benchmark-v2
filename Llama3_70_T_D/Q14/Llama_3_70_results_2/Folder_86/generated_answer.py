def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    sliced_numbers = numbers[33:37]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]