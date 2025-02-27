def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 4:
        return None
    else:
        return sorted(numbers[:4])[-2]