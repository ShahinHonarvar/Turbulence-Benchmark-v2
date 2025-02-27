from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[55]
    primes = []

    def check_truncatable(n):
        if n < 10:
            return isprime(n)
        elif '0' in str(n):
            return False
        else:
            ltr = int(str(n)[1:])
            rtr = int(str(n)[:-1])
            return isprime(n) and check_truncatable(ltr) and check_truncatable(rtr)
    for i in range(10, x + 1):
        if check_truncatable(i):
            primes.append(i)
    return sorted(primes)