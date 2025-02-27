from sympy import isprime

def all_left_right_truncatable_prime(x):
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        left_right_truncatable = True
        for i in range(len(str(num)) - 1):
            left = int(str(num)[1:])
            right = int(str(num)[:-1])
            if not isprime(left) or not isprime(right):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes