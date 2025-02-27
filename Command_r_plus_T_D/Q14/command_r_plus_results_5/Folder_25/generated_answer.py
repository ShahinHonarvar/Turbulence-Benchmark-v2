def find_second_smallest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    sub_list = numbers_list[37:77]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]