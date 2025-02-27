def gcf_three_nums(num_list):
    a = num_list[70]
    b = num_list[41]
    c = num_list[20]
    factors = []
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.append(i)
    return max(factors)