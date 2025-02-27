def if_perfect_num(int_list):
    if sum(int_list[1:]) == int_list[0]:
        return True
    else:
        return False