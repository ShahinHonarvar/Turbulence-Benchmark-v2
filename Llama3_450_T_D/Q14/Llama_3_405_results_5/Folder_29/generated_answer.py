def find_second_smallest_num(numbers):
    if len(numbers) <= 98 or 55 >= len(numbers):
        return None
    sliced_numbers = numbers[55:99]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort()
    return sliced_numbers[1]