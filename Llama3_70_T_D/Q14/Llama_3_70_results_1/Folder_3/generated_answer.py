def find_second_smallest_num(numbers):
    sliced_numbers = sorted(numbers[27:56])
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]