from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[6]
    lr_primes = []
    for num in range(1, x + 1):
        if not isprime(num):
            continue
        num_str = str(num)
        if '0' in num_str:
            continue
        for i in range(1, len(num_str)):
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[0:i])):
                break
        else:
            lr_primes.append(num)
    return sorted(lr_primes, reverse=True)