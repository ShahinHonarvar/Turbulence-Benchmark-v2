def all_left_truncatable_prime(numbers):
    x = numbers[126]
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
    return True