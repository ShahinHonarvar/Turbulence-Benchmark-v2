def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers[4:9]) < 2:
        return None
    else:
        numbers_slice = numbers[4:9]
        numbers_slice.sort()
        return numbers_slice[-2]