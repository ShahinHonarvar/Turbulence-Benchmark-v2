def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    if n < 10:
        return True
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])) or '0' in n_str[i:]:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[81]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes