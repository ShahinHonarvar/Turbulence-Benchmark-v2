def all_pos_ints_inclusive(numbers):
    if 5 <= len(numbers) < 7:
        return [num for num in numbers[5:7] if num > 0]
    else:
        return []