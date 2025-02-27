def find_second_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 6:
        return None
    else:
        sub_list = numbers_list[3:6]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None