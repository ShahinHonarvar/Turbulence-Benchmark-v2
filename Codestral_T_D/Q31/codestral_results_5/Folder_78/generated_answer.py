def if_perfect_num(num_list):
    if sum([i for i in range(1, num_list[91]) if num_list[91] % i == 0]) == num_list[91]:
        return True
    else:
        return False