def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[6]
    truncatable_primes = set()
    for num in range(10, x):
        num_str = str(num)
        if all((is_prime(int(num_str[:i + 1])) for i in range(len(num_str)))):
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)