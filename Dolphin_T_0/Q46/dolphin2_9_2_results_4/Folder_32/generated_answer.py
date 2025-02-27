def gcf_three_nums(num_list):
    a = num_list[20]
    b = num_list[43]
    c = num_list[95]
    factors = []
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.append(i)
    return max(factors)