def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable_prime(n):
    if str(n).count('0') > 0:
        return False
    for i in range(1, len(str(n)) + 1):
        if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[-i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)