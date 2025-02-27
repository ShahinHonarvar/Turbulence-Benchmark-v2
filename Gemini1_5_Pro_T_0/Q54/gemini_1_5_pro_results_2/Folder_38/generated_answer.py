def all_right_truncatable_prime(numbers):
    x = numbers[28]
    right_truncatable_primes = []
    for num in range(2, x):
        if all((isPrime(int(str(num)[:i])) for i in range(len(str(num)), 0, -1))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True