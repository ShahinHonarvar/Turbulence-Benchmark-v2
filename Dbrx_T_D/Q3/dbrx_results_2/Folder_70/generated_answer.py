def all_pos_ints_inclusive(numbers):
    if len(numbers) < 33 or not all((isinstance(i, int) for i in numbers)):
        return []
    return [num for num in numbers[27:33] if num > 0]