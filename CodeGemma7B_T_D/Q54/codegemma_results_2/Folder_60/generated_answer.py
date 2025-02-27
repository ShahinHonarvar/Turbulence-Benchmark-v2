def all_right_truncatable_prime(t):
    x = t[87]
    primes = [i for i in range(3, x + 1) if all((i % j != 0 for j in range(2, i)))]
    right_truncatable_primes = []
    for prime in primes:
        truncatable = True
        for i in range(len(str(prime)) - 1, -1, -1):
            num = int(str(prime)[:i])
            if num in [2, 3, 5, 7] or num % 2 == 0 or num % 3 == 0 or (num % 5 == 0) or (num % 7 == 0):
                truncatable = False
                break
            if not is_prime(num):
                truncatable = False
                break
        if truncatable:
            right_truncatable_primes.append(prime)
    right_truncatable_primes.sort()
    return right_truncatable_primes or []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True