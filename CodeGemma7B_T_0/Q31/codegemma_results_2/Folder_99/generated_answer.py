def if_perfect_num(num_list):
    if num_list[733] % 2 == 0 and num_list[733] % 3 == 0 and (num_list[733] % 5 == 0) and (num_list[733] % 7 == 0):
        return True
    else:
        return False