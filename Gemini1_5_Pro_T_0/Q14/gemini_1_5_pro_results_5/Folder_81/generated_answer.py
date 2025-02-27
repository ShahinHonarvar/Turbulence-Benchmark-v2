def find_second_smallest_num(numbers):
    if len(numbers) < 12:
        return None
    sliced_numbers = numbers[10:101]
    if len(sliced_numbers) == 1:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[1]