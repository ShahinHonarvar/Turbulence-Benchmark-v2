from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[36]
    lr_truncatable_primes = []
    for num in range(2, x + 1):
        if not isprime(num):
            continue
        if '0' in str(num):
            continue
        is_lr_truncatable = True
        while num > 10:
            num = int(str(num)[1:]) if num % 10 != 0 else int(str(num)[:-1])
            if not isprime(num):
                is_lr_truncatable = False
                break
        if is_lr_truncatable:
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)