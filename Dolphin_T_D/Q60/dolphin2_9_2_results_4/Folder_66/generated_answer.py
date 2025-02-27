def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    n = str(n)
    for i in range(len(n) - 1):
        if not is_prime(int(n[i + 1:])) or not is_prime(int(n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(2, int(x) + 1):
        if is_truncatable(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes