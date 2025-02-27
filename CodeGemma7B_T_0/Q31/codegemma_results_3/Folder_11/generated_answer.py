def if_perfect_num(num_list):
    if num_list[77] % 2 == 0 and num_list[77] % 3 == 0 and (num_list[77] % 5 == 0) and (num_list[77] % 7 == 0):
        return True
    else:
        return False