def find_second_smallest_num(numbers):
    if len(numbers) < 53 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    sliced_numbers = sorted(numbers[52:72])
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]