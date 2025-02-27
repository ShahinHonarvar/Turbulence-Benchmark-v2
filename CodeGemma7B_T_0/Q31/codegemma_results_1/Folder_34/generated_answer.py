def if_perfect_num(num_list):
    if num_list[97] % 2 == 0 and num_list[97] % 3 == 0 and (num_list[97] % 5 == 0) and (num_list[97] % 7 == 0):
        return True
    else:
        return False