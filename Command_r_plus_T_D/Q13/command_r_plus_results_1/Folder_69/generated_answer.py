def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    target_range = numbers[32:36]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[-2]