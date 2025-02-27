def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 91:
        return None
    numbers_slice = numbers[90:91]
    if len(numbers_slice) < 2:
        return None
    numbers_slice.sort()
    return numbers_slice[1]