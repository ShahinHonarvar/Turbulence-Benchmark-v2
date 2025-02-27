from sympy import isprime

def all_lr_truncatable_prime(bound_tuple):
    x = bound_tuple[87]
    lr_truncatable_primes = []
    for num in range(2, x + 1):
        if not isprime(num):
            continue
        str_num = str(num)
        if '0' in str_num:
            continue
        for i in range(1, len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:i])):
                break
            if i == len(str_num) - 1:
                lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes)