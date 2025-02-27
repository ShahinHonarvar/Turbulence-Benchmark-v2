def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 2:
        return None
    else:
        largest_num = max(numbers_list)
        numbers_list.remove(largest_num)
        return max(numbers_list)