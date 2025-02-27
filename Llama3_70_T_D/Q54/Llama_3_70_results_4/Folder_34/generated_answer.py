def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def all_right_truncatable_primes(numbers):
    x = numbers[18]
    return sorted([i for i in range(11, x) if is_prime(i) and is_right_truncatable(i)], reverse=True)