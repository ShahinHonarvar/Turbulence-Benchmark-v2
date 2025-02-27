def if_perfect_num(int_list):
    if int_list[37] % sum(range(1, int_list[37])) == 0:
        return True
    return False