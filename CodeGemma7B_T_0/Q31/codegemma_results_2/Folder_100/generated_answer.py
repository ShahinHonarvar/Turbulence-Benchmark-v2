def if_perfect_num(num_list):
    if num_list[99] % 2 == 0 and num_list[99] % 3 == 0 and (num_list[99] % 5 == 0) and (num_list[99] % 7 == 0):
        return True
    else:
        return False