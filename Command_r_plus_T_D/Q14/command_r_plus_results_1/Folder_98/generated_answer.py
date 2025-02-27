def find_second_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 7:
        return None
    else:
        numbers_list.sort()
        return numbers_list[6]