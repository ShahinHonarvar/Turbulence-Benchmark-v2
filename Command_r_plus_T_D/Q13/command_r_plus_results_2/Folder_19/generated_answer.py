def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 6:
        return None
    else:
        sub_list = numbers_list[3:6]
        sub_list.sort()
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[-2]