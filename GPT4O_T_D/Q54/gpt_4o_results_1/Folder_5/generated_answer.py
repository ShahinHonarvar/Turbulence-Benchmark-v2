def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(n):

    def is_right_truncatable(p):
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True
    result = []
    for i in range(2, n):
        if is_right_truncatable(i):
            result.append(i)
    return result

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 55:
        return []
    x = numbers[55]
    primes = right_truncatable_primes(x)
    return sorted(primes)