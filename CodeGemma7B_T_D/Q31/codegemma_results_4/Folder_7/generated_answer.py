def if_perfect_num(num_list):
    if num_list[851] % sum(range(1, num_list[851])) == 0:
        return True
    else:
        return False