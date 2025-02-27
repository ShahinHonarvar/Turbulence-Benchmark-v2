def all_right_truncatable_prime(numbers):
    x = numbers[945]
    primes = []
    for num in range(2, x):
        if all((isPrime(int(str(num)[:i])) for i in range(len(str(num)), 0, -1))):
            primes.append(num)
    primes.sort(reverse=True)
    return primes

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True