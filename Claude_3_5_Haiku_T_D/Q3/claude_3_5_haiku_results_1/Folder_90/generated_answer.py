def all_pos_ints_inclusive(numbers):
    if len(numbers) < 747:
        return []
    result = [num for num in numbers[262:747] if num > 0]
    return result