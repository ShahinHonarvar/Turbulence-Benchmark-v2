def all_right_truncatable_prime(numbers):
    x = numbers[14]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_right_truncatable_prime(n):
    if n < 2:
        return False
    n = str(n)
    for i in range(len(n)):
        if not is_prime(int(n[i:])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True