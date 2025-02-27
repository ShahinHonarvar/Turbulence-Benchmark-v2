from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[57]

    def is_right_truncatable_prime(n):
        while n > 1:
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    rtp = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    rtp.sort(reverse=True)
    return rtp