def if_perfect_num(num_list):
    if num_list[54] % 2 == 0:
        return True
    elif num_list[54] % 3 == 0 or num_list[54] % 5 == 0:
        return True
    else:
        return False