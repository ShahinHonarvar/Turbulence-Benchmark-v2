from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[23]
    rtp = []
    for i in range(10, x):
        if is_right_truncatable_prime(i):
            rtp.append(i)
    return sorted(rtp)

def is_right_truncatable_prime(n):
    while n > 1:
        if not isprime(n):
            return False
        n = int(str(n)[1:])
    return True