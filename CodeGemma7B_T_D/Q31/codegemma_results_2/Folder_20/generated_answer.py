def if_perfect_num(num_list):
    if num_list[53] % sum(num_list[:53]) == 0:
        return True
    else:
        return False