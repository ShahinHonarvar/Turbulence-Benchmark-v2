def all_right_truncatable_prime(numbers):
    x = numbers[41]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(num):
    if num < 2:
        return False
    for i in range(len(str(num))):
        if not is_prime(int(str(num)[:len(str(num)) - i])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True