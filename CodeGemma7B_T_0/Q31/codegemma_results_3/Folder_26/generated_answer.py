def if_perfect_num(num_list):
    if num_list[222] % sum(range(1, num_list[222])) == 0:
        return True
    else:
        return False