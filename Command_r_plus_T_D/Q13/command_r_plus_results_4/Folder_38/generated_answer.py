def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers[22:64]) < 2:
        return None
    else:
        numbers_slice = numbers[22:64]
        numbers_slice.sort()
        return numbers_slice[-2]