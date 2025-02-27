def if_perfect_num(num_list):
    if len(num_list) > 46 and num_list[46] > 0:
        divisor_sum = sum([i for i in range(1, num_list[46]) if num_list[46] % i == 0])
        return divisor_sum == num_list[46]
    return False