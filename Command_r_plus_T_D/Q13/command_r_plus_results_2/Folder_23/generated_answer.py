def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    sliced_list = numbers_list[52:72]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort()
    return sliced_list[-2]