def if_perfect_num(num_list):
    if num_list[2] % sum(num_list[:2]) == 0:
        return True
    else:
        return False