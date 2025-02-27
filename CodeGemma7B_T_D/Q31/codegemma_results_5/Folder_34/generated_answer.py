def if_perfect_num(num_list):
    return num_list[97] % (sum(range(1, num_list[97])) == 0).all()