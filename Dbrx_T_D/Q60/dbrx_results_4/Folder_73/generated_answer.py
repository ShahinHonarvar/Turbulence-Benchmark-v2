from sympy import isprime

def all_left_right_truncatable_prime(limit_tuple):
    all_primes = []
    x = min(limit_tuple[96], 1000)
    for num in range(10, x + 1):
        if not isprime(num):
            continue
        is_ltruncatable = True
        is_rtruncatable = True
        while num > 9 and is_ltruncatable and is_rtruncatable:
            num = int(str(num)[1:])
            if not isprime(num):
                is_ltruncatable = False
            num = int(str(num)[:-1])
            if not isprime(num):
                is_rtruncatable = False
        if is_ltruncatable and is_rtruncatable:
            all_primes.append(num)
    return sorted(list(set(all_primes)))