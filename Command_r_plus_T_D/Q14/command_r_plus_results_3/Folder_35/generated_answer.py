def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[15:40]) < 2:
        return None
    else:
        numbers_slice = numbers[15:40]
        numbers_slice.sort()
        return numbers_slice[1]