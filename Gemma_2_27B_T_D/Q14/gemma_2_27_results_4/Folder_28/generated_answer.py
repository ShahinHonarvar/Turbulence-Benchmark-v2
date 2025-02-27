def find_second_smallest_num(numbers):
    if len(numbers) < 50 - 22 + 1:
        return None
    slice = numbers[22:51]
    slice.sort()
    if len(slice) < 2:
        return None
    return slice[1]