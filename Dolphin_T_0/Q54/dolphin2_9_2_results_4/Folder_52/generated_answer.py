def all_right_truncatable_prime(numbers):
    x = numbers[52]
    primes = []
    if is_prime(x):
        primes.append(x)
        while primes[-1] > 1:
            primes.append(int(str(primes[-1])[:-1]))
        primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True