def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    truncatable_primes = [2, 3, 5, 7]
    for i in range(3, x):
        if is_prime(i):
            if i < 10 or (i % 10 not in [0, 3, 7] and i >= 10 and is_prime(i // 10) and is_prime(i % 10)):
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True