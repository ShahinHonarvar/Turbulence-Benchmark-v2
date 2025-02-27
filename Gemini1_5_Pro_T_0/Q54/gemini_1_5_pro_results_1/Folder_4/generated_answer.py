def all_right_truncatable_prime(numbers):
    x = numbers[96]
    right_truncatable_primes = []
    for num in range(2, x):
        if all((isPrime(n) for n in rightTruncates(num))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def rightTruncates(n):
    n = str(n)
    truncates = []
    for i in range(len(n)):
        truncates.append(int(n[:len(n) - i]))
    return truncates