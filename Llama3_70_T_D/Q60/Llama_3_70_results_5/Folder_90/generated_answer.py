def is_prime(n):
    if n < 2:
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

def truncatable(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    length = len(num_str)
    for i in range(1, length):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[466]
    truncatable_primes = [n for n in range(2, x + 1) if is_prime(n) and truncatable(n)]
    return sorted(truncatable_primes, reverse=True)