def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 9:
        return None
    else:
        numbers_slice = numbers[1:9]
        numbers_slice.sort()
        return numbers_slice[1]