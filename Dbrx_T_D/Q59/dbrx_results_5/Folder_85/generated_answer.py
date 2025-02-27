def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_left_truncatable_primes():
    result = []
    for i in range(1, 10):
        if is_prime(i):
            result.append(i)
    current = [10 * i + j for i in result for j in range(10) if is_prime(10 * i + j)]
    while current:
        result.extend(current)
        current = [10 * i + j for i in current for j in range(10) if is_prime(10 * i + j)]
    return result

def all_left_truncatable_prime(t):
    return sorted(filter(lambda x: x < t[94], get_left_truncatable_primes()))