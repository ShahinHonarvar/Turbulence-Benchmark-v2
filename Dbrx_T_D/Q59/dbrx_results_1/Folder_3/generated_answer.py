from sympy import isprime

def all_left_truncatable_prime(nums_tuple):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = nums_tuple[100]
    left_truncatable_primes = []
    for num in range(1, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes