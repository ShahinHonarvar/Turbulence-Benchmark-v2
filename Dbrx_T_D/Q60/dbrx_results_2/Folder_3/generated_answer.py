from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[100]
    lr_truncatable_primes = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        left_truncatable = True
        for i in range(1, len(str(num))):
            if not isprime(int(str(num)[i:])):
                left_truncatable = False
                break
        right_truncatable = True
        for i in range(1, len(str(num))):
            if not isprime(int(str(num)[:-i])):
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes)