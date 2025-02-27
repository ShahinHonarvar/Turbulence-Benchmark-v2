def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    sliced_numbers = numbers[25:60]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort()
    return sliced_numbers[1]