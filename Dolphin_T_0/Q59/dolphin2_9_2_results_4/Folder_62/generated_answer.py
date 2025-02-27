from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[70]
    res = []
    for i in range(1, x):
        all_trunc = [isprime(int(str(i)[j:])) for j in range(len(str(i)))]
        if all(all_trunc):
            res.append(i)
    return sorted(res)