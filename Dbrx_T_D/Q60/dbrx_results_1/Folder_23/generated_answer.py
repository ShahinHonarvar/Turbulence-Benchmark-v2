from sympy import isprime

def all_left_right_truncatable_prime(upper_bound_tuple):
    upper_bound = upper_bound_tuple[77]
    lr_truncatable_primes = []
    for num in range(2, upper_bound + 1):
        if not isprime(num):
            continue
        str_num = str(num)
        if '0' in str_num:
            continue
        is_lr_truncatable = all((isprime(int(str_num[i:j])) for i in range(len(str_num)) for j in range(i + 1, len(str_num) + 1)))
        if is_lr_truncatable:
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)