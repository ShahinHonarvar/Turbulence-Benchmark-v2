def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 11:
        return None
    else:
        sorted_list = sorted(numbers_list[:11])
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[-2]