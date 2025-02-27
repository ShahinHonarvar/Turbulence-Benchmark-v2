def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    numbers_slice = numbers[22:89]
    numbers_set = set(numbers_slice)
    if len(numbers_set) < 2:
        return None
    return sorted(numbers_set)[1]