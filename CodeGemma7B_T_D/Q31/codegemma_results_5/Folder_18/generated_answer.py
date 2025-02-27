def if_perfect_num(num_lst):
    if num_lst[312] % 2 == 0 and num_lst[312] >= 4 and (num_lst[312] % 3 != 0):
        return True
    else:
        return False