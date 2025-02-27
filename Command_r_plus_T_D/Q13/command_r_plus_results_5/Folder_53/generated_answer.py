def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    sub_list = numbers_list[100:201]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]