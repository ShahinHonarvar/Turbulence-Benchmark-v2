def if_perfect_num(int_list):
    if sum(int_list[:40]) == int_list[40]:
        return True
    else:
        return False