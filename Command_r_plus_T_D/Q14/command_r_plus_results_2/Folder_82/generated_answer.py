def find_second_smallest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    sub_list = numbers_list[20:201]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]