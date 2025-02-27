def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    sub_list = numbers_list[62:93]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]