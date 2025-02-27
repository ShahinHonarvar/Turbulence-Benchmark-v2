def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 32 >= len(numbers):
        return None
    sliced_numbers = numbers[28:33]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]