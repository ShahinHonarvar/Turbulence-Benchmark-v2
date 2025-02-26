def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[79]
    truncatable_primes = []
    for n in range(x, 11, -1):
        if '0' in str(n):
            continue
        is_lrt_prime = True
        num_str = str(n)
        for i in range(len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:len(num_str) - i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                is_lrt_prime = False
                break
        if is_lrt_prime and is_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)