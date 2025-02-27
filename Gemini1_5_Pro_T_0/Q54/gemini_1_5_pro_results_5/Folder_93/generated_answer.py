def all_right_truncatable_prime(numbers):
    x = numbers[11]
    primes = []
    for num in range(2, x):
        if all((isPrime(int(str(num)[:i + 1])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True