def find_second_smallest_num(numbers):
    if len(numbers) < 40 or 28 > len(numbers):
        return None
    sliced_numbers = numbers[28:41]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[1]