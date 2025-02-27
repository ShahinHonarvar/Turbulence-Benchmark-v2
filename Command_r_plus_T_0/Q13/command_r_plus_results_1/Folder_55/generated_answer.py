def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 11:
        return None
    numbers = sorted(numbers[:11])
    if len(numbers) < 2:
        return None
    return numbers[-2]