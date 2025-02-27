def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list or len(numbers_list) < 101:
        return None
    numbers_list = sorted(numbers_list[10:101])
    if len(numbers_list) < 2:
        return None
    return numbers_list[-2]