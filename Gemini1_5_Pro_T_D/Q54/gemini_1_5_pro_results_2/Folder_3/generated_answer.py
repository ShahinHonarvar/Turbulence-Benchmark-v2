def all_right_truncatable_prime(numbers):
    x = numbers[100]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(n):
    if n < 2:
        return False
    n_str = str(n)
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True