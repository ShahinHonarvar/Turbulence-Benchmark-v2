def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_truncatable(n):
    if n < 10:
        return True
    num_str = str(n)
    if '0' in num_str:
        return False
    for _ in range(0, len(num_str) - 2):
        if not is_prime(int(num_str[1:])):
            return False
        if not is_prime(int(num_str[:-1])):
            return False
        num_str = num_str[1:-1]
    return True

def all_left_right_truncatable_prime(num_tupl):
    primes = []
    x = num_tupl[35]
    for num in range(2, x + 1):
        if is_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)