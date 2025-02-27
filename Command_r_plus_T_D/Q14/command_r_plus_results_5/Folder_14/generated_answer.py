def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[8:10]) < 2:
        return None
    else:
        numbers_slice = numbers[8:10]
        numbers_slice.sort()
        return numbers_slice[1]