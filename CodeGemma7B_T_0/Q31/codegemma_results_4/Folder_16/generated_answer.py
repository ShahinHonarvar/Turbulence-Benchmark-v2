def if_perfect_num(num_list):
    if num_list[162] % 2 == 0 and num_list[162] % 3 == 0 and (num_list[162] % 5 == 0):
        return True
    else:
        return False