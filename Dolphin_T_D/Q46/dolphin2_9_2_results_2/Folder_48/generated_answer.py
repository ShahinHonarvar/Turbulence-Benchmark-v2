def gcf_three_nums(num_list):
    a = num_list[654]
    b = num_list[312]
    c = num_list[441]
    factors = set()
    for i in range(1, max(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.add(i)
    return max(factors)