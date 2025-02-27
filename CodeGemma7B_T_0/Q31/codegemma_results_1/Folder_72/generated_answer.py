def if_perfect_num(num_list):
    if num_list[16] % 2 == 0 and num_list[16] % 3 == 0 and (num_list[16] % 5 == 0):
        return True
    else:
        return False