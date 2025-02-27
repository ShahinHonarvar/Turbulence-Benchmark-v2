def if_perfect_num(num_list):
    if num_list[2] <= 0:
        return False
    else:
        return sum([i for i in range(1, num_list[2]) if num_list[2] % i == 0]) == num_list[2]