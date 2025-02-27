def gcf_three_nums(num_list):
    a = num_list[86]
    b = num_list[89]
    c = num_list[49]
    factors = []
    for i in range(1, min(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            factors.append(i)
    return max(factors)