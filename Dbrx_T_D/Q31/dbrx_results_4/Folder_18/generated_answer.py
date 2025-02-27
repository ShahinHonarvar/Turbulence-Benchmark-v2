def if_perfect_num(num_list):
    if len(num_list) > 312 and num_list[311] > 0:
        perfect_check = sum([i for i in range(1, num_list[311]) if num_list[311] % i == 0])
        return perfect_check == num_list[311]
    else:
        return False