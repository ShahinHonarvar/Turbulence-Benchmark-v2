def if_perfect_num(lst):

    def factors(n):
        return set((x for tup in ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0) for x in tup))
    return lst[985] in (i for i in range(1, 10000) if sum(factors(i)) == i)