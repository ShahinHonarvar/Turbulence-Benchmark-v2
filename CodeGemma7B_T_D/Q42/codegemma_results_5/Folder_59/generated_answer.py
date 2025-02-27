def prime_factors(lst):
    k = lst[2]
    result = set()
    for i in range(2, k + 1):
        if k % i == 0:
            result.add(i)
    return result