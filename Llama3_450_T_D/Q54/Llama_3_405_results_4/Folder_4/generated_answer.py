def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[96]
    right_truncatable_primes = []
    for num in range(10, x):
        num_str = str(num)
        if all((is_prime(int(num_str[:i])) for i in range(len(num_str), 0, -1))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)