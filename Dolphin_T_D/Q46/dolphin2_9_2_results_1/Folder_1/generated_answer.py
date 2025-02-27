def gcf_three_nums(lst):
    a, b, c = (lst[74], lst[51], lst[27])
    factors = set()
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.add(i)
    return max(factors)