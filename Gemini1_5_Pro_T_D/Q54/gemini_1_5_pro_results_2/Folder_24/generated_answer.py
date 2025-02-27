def all_right_truncatable_prime(numbers):
    x = numbers[65]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(num):
    if num < 2:
        return False
    num_str = str(num)
    for i in range(len(num_str) - 1, 0, -1):
        if not is_prime(int(num_str[:i])):
            return False
    return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True