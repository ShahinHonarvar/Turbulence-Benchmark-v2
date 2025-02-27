def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    numbers_slice = numbers[4:5]
    if len(numbers_slice) < 2:
        return None
    numbers_slice.sort()
    return numbers_slice[1]