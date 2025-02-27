def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[22:51]) < 2:
        return None
    else:
        numbers_slice = numbers[22:51]
        numbers_slice.sort()
        return numbers_slice[1]