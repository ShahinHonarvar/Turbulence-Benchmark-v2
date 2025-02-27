def if_perfect_num(num_list):
    if num_list[478] == 0:
        return False
    else:
        perfect_num = True
        for i in range(2, num_list[478]):
            if num_list[478] % i == 0:
                perfect_num = False
        if perfect_num:
            return True
        else:
            return False