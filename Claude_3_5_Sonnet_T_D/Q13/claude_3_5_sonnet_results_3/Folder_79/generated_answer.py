def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    slice = numbers[4:5]
    if len(slice) < 2:
        return None
    return sorted(slice, reverse=True)[1] if len(slice) >= 2 else None