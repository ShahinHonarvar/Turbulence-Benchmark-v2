def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 11:
        return None
    else:
        numbers_slice = numbers[10:11]
        if len(numbers_slice) < 2:
            return None
        else:
            numbers_slice.sort()
            return numbers_slice[1]