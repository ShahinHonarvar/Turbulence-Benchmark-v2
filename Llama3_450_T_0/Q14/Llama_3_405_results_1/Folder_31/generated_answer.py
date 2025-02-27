def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 93 >= len(numbers) or 29 < 0:
        return None
    sliced_numbers = numbers[29:94]
    sorted_numbers = sorted(sliced_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]