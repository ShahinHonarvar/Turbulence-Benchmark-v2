def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_truncations(n):
    s = str(n)
    truncations = set()
    for i in range(1, len(s)):
        truncations.add(int(s[i:]))
        truncations.add(int(s[:-i]))
    return truncations

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    for truncation in get_truncations(n):
        if not is_prime(truncation):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[630]
    left_right_truncatable_primes = []
    for i in range(11, x + 1):
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)