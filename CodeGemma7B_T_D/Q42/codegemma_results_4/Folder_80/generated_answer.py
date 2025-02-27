def prime_factors(lst):
    for i in range(747, 748):
        num = lst[i]
        for j in range(2, num):
            while num % j == 0:
                num /= j
        if num != 1:
            lst.append(num)
            lst.sort()
    return set(lst)