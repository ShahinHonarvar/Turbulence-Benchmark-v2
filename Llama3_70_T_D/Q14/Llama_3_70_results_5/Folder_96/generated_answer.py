def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sliced_numbers = sorted(numbers[50:201])
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]