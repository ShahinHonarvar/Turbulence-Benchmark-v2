def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    primes = []
    for n in range(x - 1, 1, -1):
        if '0' in str(n):
            continue
        while n:
            if is_prime(n):
                primes.append(n)
            n //= 10
    return sorted(primes, reverse=True)