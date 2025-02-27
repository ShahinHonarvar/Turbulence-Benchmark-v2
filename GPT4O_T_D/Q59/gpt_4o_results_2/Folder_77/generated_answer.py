def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[767]
    left_truncatable_primes = []
    for number in range(2, x):
        if '0' not in str(number) and is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes, reverse=True)