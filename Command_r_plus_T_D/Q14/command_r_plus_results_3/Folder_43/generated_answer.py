def find_second_smallest_num(numbers_list: list[int]) -> int:
    try:
        sliced_list = numbers_list[74:96]
        sliced_list.sort()
        return sliced_list[1]
    except IndexError:
        return None