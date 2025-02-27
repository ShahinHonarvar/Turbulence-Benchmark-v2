def find_second_smallest_num(numbers):
    if len(numbers) < 924 or len(numbers) <= 661:
        return None
    numbers_slice = numbers[661:925]
    numbers_slice.sort()
    if len(numbers_slice) < 2:
        return None
    return numbers_slice[1]