def find_second_largest_num(list_of_num):
    num_len = len(list_of_num)
    if num_len < 70:
        return None
    max_num = max(list_of_num)
    list_of_num.remove(max_num)
    return max(list_of_num[63:67])