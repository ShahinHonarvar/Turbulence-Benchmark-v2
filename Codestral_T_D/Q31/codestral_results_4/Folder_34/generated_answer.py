def if_perfect_num(num_list):
    if sum((i for i in range(1, num_list[97]) if num_list[97] % i == 0)) == num_list[97]:
        return True
    else:
        return False