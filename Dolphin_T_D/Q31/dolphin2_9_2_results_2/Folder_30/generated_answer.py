def if_perfect_num(num_list):
    if sum(num_list[:num_list[94]]) == num_list[94]:
        return True
    else:
        return False