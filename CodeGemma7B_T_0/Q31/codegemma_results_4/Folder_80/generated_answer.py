def if_perfect_num(num_list):
    if num_list[746] % sum(num_list[:746]) == 0:
        return True
    else:
        return False