def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    else:
        return sorted(numbers[:5])[-2]