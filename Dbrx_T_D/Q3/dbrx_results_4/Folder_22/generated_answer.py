def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 201 and len(numbers) >= 40:
        return [num for num in numbers[40:201] if num > 0]
    else:
        return []