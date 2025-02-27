def find_second_smallest_num(numbers_list: list[int]) -> int:
    sliced_list = numbers_list[75:86]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]