def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 6 or len(set(numbers_list[:6])) < 3:
        return None
    else:
        sub_list = sorted(numbers_list[3:6])
        return sub_list[-2]