from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[7]
    left_truncatable_primes = []
    for num in range(11, x):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_left_truncatable_prime = True
        while len(num_str) > 0:
            if not isprime(int(num_str)):
                is_left_truncatable_prime = False
                break
            num_str = num_str[1:]
        if is_left_truncatable_prime:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)