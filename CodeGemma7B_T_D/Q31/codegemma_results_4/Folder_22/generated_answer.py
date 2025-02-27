def if_perfect_num(int_list):
    if int_list[72] % sum(int_list[72] // 2) == 0:
        return True
    return False