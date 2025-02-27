def if_perfect_num(int_list):
    if int_list[733] % sum([x for x in range(int_list[733]) if x != 0]) == 0:
        return True
    else:
        return False