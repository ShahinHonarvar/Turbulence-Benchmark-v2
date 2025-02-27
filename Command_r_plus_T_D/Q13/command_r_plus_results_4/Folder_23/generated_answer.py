def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    start_index = 52
    end_index = 71
    numbers_range = numbers_list[start_index:end_index + 1]
    if len(numbers_range) < 2:
        return None
    numbers_range.sort()
    return numbers_range[-2]