from sympy import isprime

def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[64]
    lr_primes = []

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        if not isprime(num):
            return False
        for i in range(1, len(str(num))):
            if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            lr_primes.append(num)
    return sorted(lr_primes, reverse=True)