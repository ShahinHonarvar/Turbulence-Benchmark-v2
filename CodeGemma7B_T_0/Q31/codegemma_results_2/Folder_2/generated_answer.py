def if_perfect_num(num_list):
    if num_list[702] % 2 == 0 and num_list[702] % 3 == 0 and (num_list[702] % 5 == 0) and (num_list[702] % 7 == 0):
        return True
    else:
        return False