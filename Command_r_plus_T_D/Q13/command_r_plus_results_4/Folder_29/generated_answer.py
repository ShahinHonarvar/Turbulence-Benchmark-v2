def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 98 or len(numbers) < 59:
        return None
    target_range = numbers[59:98]
    target_range.sort()
    if len(target_range) < 2:
        return None
    return target_range[-2]