def find_second_smallest_num(numbers):
    if len(numbers) <= 200:
        return None
    numbers_slice = numbers[20:201]
    numbers_slice.sort()
    if len(numbers_slice) < 2:
        return None
    return numbers_slice[1]