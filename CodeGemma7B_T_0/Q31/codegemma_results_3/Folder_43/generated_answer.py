def if_perfect_num(num_list):
    if num_list[29] % 2 == 0 and num_list[29] % 3 == 0 and (num_list[29] % 5 == 0):
        return True
    else:
        return False