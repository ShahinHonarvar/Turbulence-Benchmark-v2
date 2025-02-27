def find_second_smallest_num(numbers_list: list[int]) -> int:
    sub_list = numbers_list[35:50]
    sub_list.sort()
    if len(sub_list) > 1:
        return sub_list[1]
    else:
        return None