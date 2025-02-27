def find_second_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 8:
        return None
    else:
        sub_list = numbers_list[5:8]
        sub_list.sort()
        return sub_list[1]