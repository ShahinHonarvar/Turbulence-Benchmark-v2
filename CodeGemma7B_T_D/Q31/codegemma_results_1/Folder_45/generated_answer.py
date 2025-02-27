def if_perfect_num(num_list):
    if len(num_list) >= 33 and num_list[33] % 2 != 0 and (num_list[33] % 3 != 0) and (num_list[33] ** 0.5 % int(num_list[33] ** 0.5) != 0):
        return True
    else:
        return False