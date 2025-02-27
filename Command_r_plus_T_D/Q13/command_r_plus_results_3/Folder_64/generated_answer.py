def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    numbers_slice = numbers[:5]
    numbers_slice.sort()
    return numbers_slice[-2]