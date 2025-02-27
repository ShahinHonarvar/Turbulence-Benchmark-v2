def all_pos_ints_exclusive(numbers):
    if 598 <= len(numbers) >= 767:
        return [num for num in numbers[598:767] if num > 0]
    else:
        return []