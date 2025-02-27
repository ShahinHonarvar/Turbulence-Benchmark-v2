def if_perfect_num(num_list):
    if num_list[10] % sum((i for i in range(1, num_list[10]) if num_list[10] % i == 0)) == 0:
        return True
    else:
        return False