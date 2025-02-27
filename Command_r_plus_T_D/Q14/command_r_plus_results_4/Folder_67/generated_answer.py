def find_second_smallest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    sub_list = sorted(numbers_list[50:55])
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]