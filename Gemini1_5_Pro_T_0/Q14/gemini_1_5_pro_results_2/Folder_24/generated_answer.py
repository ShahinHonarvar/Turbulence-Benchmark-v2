def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 23 >= len(numbers) or 23 < 0:
        return None
    sliced_numbers = numbers[23:24]
    if len(sliced_numbers) < 1:
        return None
    return sorted(sliced_numbers)[0]