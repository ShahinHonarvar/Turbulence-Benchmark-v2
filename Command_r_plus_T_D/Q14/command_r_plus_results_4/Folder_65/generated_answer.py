def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 58:
        return None
    else:
        numbers_slice = numbers[56:58]
        numbers_slice.sort()
        return numbers_slice[1]