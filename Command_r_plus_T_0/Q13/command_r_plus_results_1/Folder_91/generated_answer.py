def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 6:
        return None
    numbers = sorted(numbers[:6])
    if numbers[-1] == numbers[-2]:
        return None
    return numbers[-2]