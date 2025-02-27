from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[79]
    primes = []
    for num in range(1, x):
        string_num = str(num)
        if is_truncatable_prime(string_num):
            primes.append(int(string_num))
    primes.sort(reverse=True)
    return primes

def is_truncatable_prime(num):
    if not isprime(num):
        return False
    while num > 10:
        num = int(num[1:])
        if not isprime(num):
            return False
    return True