def if_perfect_num(num_list):
    if num_list[92] % 2 == 0 and num_list[92] % 3 == 0 and (num_list[92] % 5 == 0) and (num_list[92] % 7 == 0):
        return True
    else:
        return False