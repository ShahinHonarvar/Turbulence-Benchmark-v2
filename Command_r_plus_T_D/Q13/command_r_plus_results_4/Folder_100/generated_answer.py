def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    try:
        sub_list = num_list[42:69]
        sub_list.sort()
        return sub_list[-2]
    except IndexError:
        return None