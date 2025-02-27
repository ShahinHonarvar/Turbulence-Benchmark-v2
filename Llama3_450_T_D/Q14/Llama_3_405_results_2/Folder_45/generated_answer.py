def find_second_smallest_num(numbers):
    if len(numbers) < 201 or 30 > len(numbers):
        return None
    sliced_numbers = numbers[30:201]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[1]