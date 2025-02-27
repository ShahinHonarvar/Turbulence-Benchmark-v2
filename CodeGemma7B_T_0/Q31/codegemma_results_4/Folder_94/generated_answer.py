def if_perfect_num(num_list):
    if num_list[93] % 2 == 0 and num_list[93] % 3 == 0 and (num_list[93] % 5 == 0) and (num_list[93] % 7 == 0):
        return True
    else:
        return False