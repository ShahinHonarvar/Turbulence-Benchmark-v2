def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[630]
    right_truncatable_primes = set()
    for i in range(2, x):
        num_str = str(i)
        if all((is_prime(int(num_str[:j + 1])) for j in range(len(num_str)))):
            right_truncatable_primes.add(i)
    return sorted(list(right_truncatable_primes), reverse=True)