def find_second_smallest_num(numbers):
    if len(numbers) < 69 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    subset = numbers[42:69]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]