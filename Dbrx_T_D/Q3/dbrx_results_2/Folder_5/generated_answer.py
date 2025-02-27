def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 10 and all((isinstance(i, int) for i in numbers[8:10])) and all((i > 0 for i in numbers[8:10])):
        return [num for num in numbers[8:10] if num > 0]
    else:
        return []