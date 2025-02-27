def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 64:
        return None
    else:
        sub_list = numbers_list[62:64]
        sub_list.sort()
        return sub_list[1]