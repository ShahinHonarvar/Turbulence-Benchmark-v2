def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[73]
    left_truncatable_primes = [num for num in range(x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes, reverse=True)