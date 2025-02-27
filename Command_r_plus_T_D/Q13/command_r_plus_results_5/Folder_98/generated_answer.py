def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 7:
        return None
    numbers_slice = sorted(numbers[:7])
    if len(numbers_slice) < 2:
        return None
    return numbers_slice[-2]