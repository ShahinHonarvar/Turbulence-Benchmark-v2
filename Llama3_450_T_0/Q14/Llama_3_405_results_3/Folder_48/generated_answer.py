def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 750 >= len(numbers) or 246 < 0:
        return None
    sliced_numbers = numbers[246:751]
    sorted_numbers = sorted(sliced_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]