def prime_factors(lst):
    for number in lst:
        if number == lst[73]:
            for factor in range(2, int(lst[73] / 2) + 1):
                if lst[73] % factor == 0:
                    lst[73] = lst[73] / factor
    return set(lst)