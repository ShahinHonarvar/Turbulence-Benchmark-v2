def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 8:
        return None
    numbers = sorted(numbers[:8])
    if numbers[-1] == numbers[-2]:
        return None
    else:
        return numbers[-2]