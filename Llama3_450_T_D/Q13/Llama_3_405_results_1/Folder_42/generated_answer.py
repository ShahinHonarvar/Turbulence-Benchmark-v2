def find_second_largest_num(numbers):
    if len(numbers) < 80:
        return None
    numbers_slice = numbers[29:80]
    if len(numbers_slice) < 2:
        return None
    numbers_slice.sort()
    return numbers_slice[-2]