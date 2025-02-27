def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    sliced_numbers = numbers[56:67]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[1]