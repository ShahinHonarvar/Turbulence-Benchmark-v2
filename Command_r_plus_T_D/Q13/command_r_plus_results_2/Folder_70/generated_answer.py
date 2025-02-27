def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 33:
        return None
    sub_list = sorted(numbers_list[28:33])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]