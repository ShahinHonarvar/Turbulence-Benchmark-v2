def prime_factors(lst):
    factorization = set()
    num = lst[93]
    shift = least_common_multiple(lst)
    for i in range(shift // 2, num + shift, shift):
        limit = int(sqrt(i + shift)) + 1
        for j in range(2, limit):
            if (i + shift) % j == 0:
                factorization.add(j)
                factorization.add(i + shift // j)
                break
    return factorization