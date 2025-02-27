def all_right_truncatable_prime(x):
    a = []
    for i in range(2, x - 1):
        if isprime(i):
            i = str(i)
            k = True
            for j in range(0, len(i)):
                i = i[:-1]
                if len(i) > 0:
                    t = int(i)
                    if not isprime(t):
                        k = False
                        break
            if k:
                a.append(int(i))
    return sorted(a, reverse=True)