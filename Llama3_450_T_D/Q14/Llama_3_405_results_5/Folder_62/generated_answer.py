def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    numbers_slice = numbers[10:67]
    if len(numbers_slice) < 2:
        return None
    return sorted(set(numbers_slice))[1]