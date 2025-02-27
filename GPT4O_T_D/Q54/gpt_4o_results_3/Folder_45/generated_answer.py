def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    num_str = str(n)
    while len(num_str) > 1:
        num_str = num_str[:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[61]
    primes = []
    for num in range(2, x):
        if right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)