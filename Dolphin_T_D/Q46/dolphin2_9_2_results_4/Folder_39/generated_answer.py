def gcf_three_nums(l):
    a = l[85]
    b = l[36]
    c = l[54]
    factors = set()
    for i in range(1, min(a, b, c)):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.add(i)
    return max(factors)