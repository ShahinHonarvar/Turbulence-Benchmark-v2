def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    target_slice = numbers[31:35]
    if len(target_slice) < 2:
        return None
    target_slice.sort()
    return target_slice[-2]