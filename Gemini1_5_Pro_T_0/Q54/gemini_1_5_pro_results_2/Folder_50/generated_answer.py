def all_right_truncatable_prime(numbers):
    x = numbers[57]
    right_truncatable_primes = []
    for i in range(2, x):
        if all((isPrime(int(str(i)[:j])) for j in range(len(str(i)), 0, -1))):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True