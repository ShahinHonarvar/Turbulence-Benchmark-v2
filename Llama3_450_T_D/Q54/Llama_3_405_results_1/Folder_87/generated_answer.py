def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    right_truncatable_primes = []
    for num in range(10, x):
        num_str = str(num)
        if all((is_prime(int(num_str[:-i])) for i in range(len(num_str)))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)