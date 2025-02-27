from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[88]
    left_right_trunc_primes = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        num_len = len(str(num))
        is_l_r_trunc_prime = all((isprime(int(str(num)[i:j])) for i in range(num_len) for j in range(i + 1, num_len + 1)))
        if is_l_r_trunc_prime:
            left_right_trunc_primes.append(num)
    return sorted(left_right_trunc_primes, reverse=True)