def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    if len(str_n) == 1:
        return is_prime(n)
    return is_prime(n) and is_left_right_truncatable(int(str_n[1:-1]))

def all_left_right_truncatable_prime(numbers):
    x = numbers[4]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)