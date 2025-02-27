def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncate_left_right(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        yield int(n_str[i + 1:])
        yield int(n_str[:len(n_str) - i - 1])

def all_left_right_truncatable_prime(numbers):
    x = numbers[23]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            truncatables = [t for t in truncate_left_right(num) if t >= 10]
            if all((is_prime(t) for t in truncatables)):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)