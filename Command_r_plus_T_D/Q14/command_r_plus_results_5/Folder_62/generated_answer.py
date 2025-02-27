def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers[10:67]:
        return None
    numbers_slice = sorted(numbers[10:67])
    if len(numbers_slice) < 2:
        return None
    return numbers_slice[1]