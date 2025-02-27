from sympy import isprime

def all_left_right_truncatable_prime(args):
    left_right_truncatable_primes = []
    x = args[945]
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_left_right_truncatable(num):
    while num > 10 and is_prime(num):
        if '0' in str(num):
            return False
        num = int(str(num)[1:]) if num % 10 != 0 else int(str(num)[:-1])
    return is_prime(num)

def is_prime(num):
    return isprime(num)