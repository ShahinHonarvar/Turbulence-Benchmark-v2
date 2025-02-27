from sympy import isprime

def all_left_right_truncatable_prime(n_tuple):
    n = n_tuple[38]
    lr_primes = []
    for num in range(2, n + 1):
        if not isprime(num):
            continue
        if '0' in str(num):
            continue
        digits = len(str(num))
        numb_left = [int(str(num)[i:]) for i in range(digits - 1, -1, -1)]
        numb_right = [int(str(num)[:i + 1]) for i in range(digits)]
        is_lr_prime = True
        for left in numb_left:
            if not isprime(left):
                is_lr_prime = False
                break
        if not is_lr_prime:
            continue
        for right in numb_right:
            if not isprime(right):
                is_lr_prime = False
                break
        if not is_lr_prime:
            continue
        lr_primes.append(num)
    return sorted(lr_primes, reverse=True)