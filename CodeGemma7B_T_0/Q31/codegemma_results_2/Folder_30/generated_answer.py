def if_perfect_num(num_list):
    if num_list[94] % 2 == 0 and num_list[94] % 3 == 0 and (num_list[94] % 5 == 0) and (num_list[94] % 7 == 0):
        return True
    else:
        return False