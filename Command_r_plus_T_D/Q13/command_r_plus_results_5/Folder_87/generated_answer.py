def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    target_range = numbers_list[36:47]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[-2]