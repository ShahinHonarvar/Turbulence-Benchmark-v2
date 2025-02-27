from sympy import isprime

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[177]
    l_r_truncatable_primes = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        num_str = str(num)
        is_l_r_truncatable = True
        for i in range(1, len(num_str)):
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[:i])):
                is_l_r_truncatable = False
                break
        if is_l_r_truncatable:
            l_r_truncatable_primes.append(num)
    return sorted(l_r_truncatable_primes)