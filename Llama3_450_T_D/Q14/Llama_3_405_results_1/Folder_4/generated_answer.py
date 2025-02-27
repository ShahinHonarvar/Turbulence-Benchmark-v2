def find_second_smallest_num(numbers):
    if len(numbers) < 85:
        return None
    sliced_numbers = numbers[70:85]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[1]