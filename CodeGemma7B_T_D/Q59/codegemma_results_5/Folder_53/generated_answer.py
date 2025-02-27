from math import log

def all_left_truncatable_prime(args):
    p = [True] * max(args)
    p[0] = p[1] = False
    for i in range(2, int(log(max(args), 2)) + 1):
        if p[i]:
            for j in range(i * i, max(args), i):
                p[j] = False
    primes = [i for i, x in enumerate(p) if x]

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0' or not p[int(str_n[i:])]:
                return False
        return True
    result = [i for i in primes if is_truncatable_prime(i) and i < args[86]]
    return sorted(result, reverse=True)