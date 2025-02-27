def if_perfect_num(num_list):
    if sum((i for i in range(1, num_list[222]) if num_list[222] % i == 0)) == num_list[222]:
        return True
    else:
        return False