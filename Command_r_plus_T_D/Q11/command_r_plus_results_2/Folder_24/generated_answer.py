def find_largest_num(numbers_list):
    if len(numbers_list) < 96:
        return None
    return max(numbers_list[74:96])