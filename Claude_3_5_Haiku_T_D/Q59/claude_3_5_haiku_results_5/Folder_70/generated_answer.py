def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[433]
    left_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        if '0' in str(n):
            continue
        is_truncatable = True
        current = n
        while current > 0:
            if not is_prime(current):
                is_truncatable = False
                break
            current //= 10
        if is_truncatable:
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)