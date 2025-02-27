from sympy import isprime

def all_right_truncatable_prime(t):

    def f(n):
        if len(str(n)) <= 1:
            return False
        for i in range(len(str(n)) - 1, 0, -1):
            if not isprime(int(str(n)[:i])):
                return False
        return True
    ans = [int(i) for i in t if f(int(i))]
    return sorted(ans, reverse=True) if ans else []