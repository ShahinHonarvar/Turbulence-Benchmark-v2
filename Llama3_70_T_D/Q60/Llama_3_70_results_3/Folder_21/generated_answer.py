def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    n_digits = len(n_str)
    for i in range(1, n_digits):
        if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and left_right_truncatable(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)