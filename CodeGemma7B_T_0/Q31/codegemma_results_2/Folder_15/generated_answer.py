def if_perfect_num(num_list):
    if num_list[10] % 2 == 0 and num_list[10] % 3 == 0 and (num_list[10] % 5 == 0):
        return True
    else:
        return False