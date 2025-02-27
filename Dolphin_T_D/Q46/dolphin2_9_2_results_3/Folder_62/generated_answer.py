def gcf_three_nums(lst):
    a = lst[10]
    b = lst[55]
    c = lst[36]
    factors = set((fact for i in range(1, max(a, b, c) + 1) if a % i == b % i == c % i == 0 for fact in [i]))
    return max(factors)