def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    slice = numbers[56:58]
    if len(slice) < 2:
        return None
    return min(slice)