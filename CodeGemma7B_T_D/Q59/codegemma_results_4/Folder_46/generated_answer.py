def all_left_truncatable_prime(tup):
    ans = []
    x = tup[33]

    def isprime(i):
        if i <= 1:
            return False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                return False
        return True

    def leftshift(i):
        strg = str(i)
        return int(strg[1:])
    for i in range(2, x):
        strg = str(i)
        if '0' in strg:
            continue
        if isprime(i):
            ok = True
            for j in range(1, len(strg)):
                if not isprime(leftshift(i)):
                    ok = False
                    break
            if ok:
                ans.append(i)
    ans.sort()
    return ans