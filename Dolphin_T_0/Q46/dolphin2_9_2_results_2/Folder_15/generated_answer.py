def gcf_three_nums(lst):
    a = lst[4]
    b = lst[0]
    c = lst[8]
    factors = []
    for i in range(1, min(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            factors.append(i)
    return max(factors)