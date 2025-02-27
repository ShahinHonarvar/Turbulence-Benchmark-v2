def find_second_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 64:
        return None
    else:
        sliced_list = numbers_list[62:64]
        sliced_list.sort()
        return sliced_list[1] if len(sliced_list) > 1 else None