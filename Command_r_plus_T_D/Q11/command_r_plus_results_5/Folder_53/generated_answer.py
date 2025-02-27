def find_largest_num(numbers_list):
    if len(numbers_list) > 111:
        return max(numbers_list[110:112])
    else:
        return None