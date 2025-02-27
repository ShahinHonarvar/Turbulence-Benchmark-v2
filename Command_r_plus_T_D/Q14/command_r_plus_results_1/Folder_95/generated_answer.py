def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    target_range = numbers[75:86]
    unique_target_range = set(target_range)
    if len(unique_target_range) < 2:
        return None
    target_range.sort()
    return target_range[1]