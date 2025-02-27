def find_second_largest_num(num_list):
    if len(num_list) <= 94 or num_list[75] - num_list[94] >= 2:
        return None
    num_list = sorted(num_list[75:95], reverse=True)
    return num_list[1]