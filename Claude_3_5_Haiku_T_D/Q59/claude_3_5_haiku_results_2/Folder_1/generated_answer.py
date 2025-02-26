def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[20]
    left_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        str_n = str(n)
        if '0' in str_n:
            continue
        is_truncatable = True
        for i in range(1, len(str_n)):
            trunc_num = int(str_n[i:])
            if not is_prime(trunc_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(n):
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)