def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[50]
    right_trunc_primes = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            num_str = str(n)
            is_right_truncatable = True
            for l in range(1, len(num_str)):
                truncated = int(num_str[:-l])
                if not is_prime(truncated):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_trunc_primes.append(n)
    return sorted(right_trunc_primes, reverse=True)