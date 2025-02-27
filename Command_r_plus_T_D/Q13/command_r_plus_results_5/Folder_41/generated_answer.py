def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 6:
        return None
    else:
        return sorted(numbers[6:7])[-2]