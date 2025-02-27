def all_pos_ints_exclusive(numbers):
    if len(numbers) >= 10 and all((isinstance(i, int) for i in numbers)) and any((i > 0 for i in numbers[8:9])):
        return [i for i in numbers[8:9] if i > 0]
    else:
        return []