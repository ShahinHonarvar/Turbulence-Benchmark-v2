def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[760]
    right_truncatable_primes = []
    for i in range(2, x):
        num_str = str(i)
        if all((is_prime(int(num_str[:-j])) for j in range(1, len(num_str)))):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)