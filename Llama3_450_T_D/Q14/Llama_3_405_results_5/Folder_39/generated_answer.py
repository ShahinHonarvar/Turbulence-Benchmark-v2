def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 40 > len(numbers) - 1:
        return None
    sliced_numbers = numbers[28:41]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]