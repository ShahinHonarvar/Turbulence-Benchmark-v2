def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[23]
    right_truncatable_primes = []
    for num in range(2, x):
        candidate = num
        is_right_truncatable = True
        while candidate > 0:
            if not is_prime(candidate):
                is_right_truncatable = False
                break
            candidate //= 10
        if is_right_truncatable and num > 0:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)