def if_perfect_num(int_list):
    if int_list[95] % 2 == 0:
        return True
    elif int_list[95] % 3 == 0:
        return True
    elif int_list[95] % 5 == 0:
        return True
    elif int_list[95] % 7 == 0:
        return True
    else:
        return False