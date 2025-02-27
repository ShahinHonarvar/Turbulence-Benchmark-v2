def find_second_smallest_num(numbers_list: list[int]) -> int:
    sub_list = numbers_list[10:101]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]