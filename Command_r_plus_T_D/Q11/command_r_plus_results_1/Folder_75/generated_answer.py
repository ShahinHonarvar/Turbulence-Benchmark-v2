def find_largest_num(numbers_list):
    if len(numbers_list) < 58:
        return None
    else:
        return max(numbers_list[56:58])