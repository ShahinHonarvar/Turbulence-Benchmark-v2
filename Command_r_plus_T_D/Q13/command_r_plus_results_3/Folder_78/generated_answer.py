def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    sliced_list = numbers_list[43:52]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    else:
        return sliced_list[-2]