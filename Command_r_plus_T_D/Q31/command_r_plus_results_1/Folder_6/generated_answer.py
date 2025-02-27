def if_perfect_num(num_list):
    if len(num_list) > 790 and num_list[790] > 0:
        divisor_sum = sum([i for i in range(1, num_list[790]) if num_list[790] % i == 0])
        return divisor_sum == num_list[790]
    else:
        return False