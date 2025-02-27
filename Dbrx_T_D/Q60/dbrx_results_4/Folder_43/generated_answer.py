from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[89]
    ltr_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            ltr_primes.append(num)
    return sorted(ltr_primes, reverse=True)

def is_left_right_truncatable_prime(n):
    if '0' in str(n) or not isprime(n):
        return False
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not isprime(n):
            return False
        n = int(str(n)[:-1])
        if not isprime(n):
            return False
    return True