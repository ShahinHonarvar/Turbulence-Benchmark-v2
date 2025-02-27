from sympy import isprime

def all_left_right_truncatable_prime(bounds_tuple):
    x = bounds_tuple[29]
    lr_primes = []
    for num in range(1, x + 1):
        if not isprime(num):
            continue
        num_str = str(num)
        if '0' in num_str:
            continue
        is_lr_prime = True
        while num_str:
            if not isprime(int(num_str)):
                is_lr_prime = False
                break
            num_str = num_str[1:] if len(num_str) > 2 else ''
            if not num_str:
                break
            if not isprime(int(num_str)):
                is_lr_prime = False
                break
            num_str = num_str[:-1]
        if is_lr_prime:
            lr_primes.append(num)
    return sorted(lr_primes)