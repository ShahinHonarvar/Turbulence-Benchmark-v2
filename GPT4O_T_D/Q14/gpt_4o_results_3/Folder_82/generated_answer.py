def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sliced_numbers = numbers[20:201]
    unique_numbers = sorted(set(sliced_numbers))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]