def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[466]
    right_truncatable_primes = set()
    for num in range(10, x):
        num_str = str(num)
        if all((is_prime(int(num_str[:-i])) for i in range(len(num_str)))):
            right_truncatable_primes.add(num)
    right_truncatable_primes = sorted(list(right_truncatable_primes), reverse=True)
    return right_truncatable_primes