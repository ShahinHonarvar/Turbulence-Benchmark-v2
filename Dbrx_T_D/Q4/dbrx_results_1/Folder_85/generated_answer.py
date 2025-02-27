def all_pos_ints_exclusive(numbers):
    if len(numbers) >= 6 and all((isinstance(num, int) for num in numbers[4:6])) and all((num > 0 for num in numbers[4:6])):
        return [num for num in numbers[4:6] if num > 0]
    else:
        return []