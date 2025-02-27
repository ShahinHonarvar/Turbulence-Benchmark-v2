def if_perfect_num(num_list):
    if num_list[94] % 1 == 0 and num_list[94] % num_list[94] == 0 and (num_list[94] > 0):
        return True
    return False