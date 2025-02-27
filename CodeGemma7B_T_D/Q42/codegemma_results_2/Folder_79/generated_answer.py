def prime_factors(lst):
    factor_set = set()
    target_num = lst[63]
    for i in range(2, target_num + 1):
        while target_num % i == 0:
            factor_set.add(i)
            target_num //= i
    return factor_set