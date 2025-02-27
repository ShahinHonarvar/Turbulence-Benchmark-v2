from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_prime(n):
        return isprime(n) and all((int(d) for d in str(n) if d != '0'))
    res = []
    for x in range(2, t[0]):
        if is_prime(x) and is_prime(int(str(x)[:-1])):
            if is_prime(int(str(x)[1:])):
                res.append(x)
    return sorted(res) if res else []