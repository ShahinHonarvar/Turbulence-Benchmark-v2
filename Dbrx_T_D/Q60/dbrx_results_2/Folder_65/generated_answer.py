from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[32]
    l_r_truncatable_primes = []
    for num in range(2, x + 1):
        if not isprime(num):
            continue
        num_str = str(num)
        if '0' in num_str:
            continue
        is_l_r_truncatable_prime = True
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not isprime(int(num_str)):
                is_l_r_truncatable_prime = False
                break
        if is_l_r_truncatable_prime:
            l_r_truncatable_primes.append(num)
    return sorted(l_r_truncatable_primes)