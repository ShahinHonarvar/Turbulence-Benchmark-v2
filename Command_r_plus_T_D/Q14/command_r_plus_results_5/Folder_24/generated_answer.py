def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 23:
        return None
    else:
        numbers_slice = numbers[23:24]
        if len(numbers_slice) < 2:
            return None
        else:
            numbers_slice.sort()
            return numbers_slice[1]