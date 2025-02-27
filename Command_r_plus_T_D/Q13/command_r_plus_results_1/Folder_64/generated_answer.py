def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    numbers_slice = sorted(numbers[:5])
    if len(numbers_slice) < 2:
        return None
    return numbers_slice[-2]