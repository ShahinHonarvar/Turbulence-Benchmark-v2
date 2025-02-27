def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 10:
        return None
    num_list.sort()
    return num_list[-2]