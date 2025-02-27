def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 11:
        return None
    else:
        numbers_list.sort()
        return numbers_list[-2]