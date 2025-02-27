def find_primes_between_indices(lst):
    res = []
    for i in range(415, 648):
        n = lst[i]
        if n > 1:
            flag = True
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    flag = False
                    break
            if flag:
                res.append(n)
    res.sort()
    return res