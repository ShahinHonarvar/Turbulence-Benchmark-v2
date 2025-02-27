from sympy import isprime

def all_left_right_truncatable_prime(n_tuple):
    n = n_tuple[975]
    lr_truncatable_primes = []
    for num in range(2, n + 1):
        if not isprime(num):
            continue
        num_str = str(num)
        if '0' in num_str:
            continue
        is_lr_truncatable = True
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not isprime(int(num_str)):
                is_lr_truncatable = False
                break
        if is_lr_truncatable:
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)