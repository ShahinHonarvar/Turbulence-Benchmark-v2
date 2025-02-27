def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 7:
        return None
    else:
        return sorted(numbers[6:7])[-2]