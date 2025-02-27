def all_right_truncatable_prime(t):
    x = t[87]
    primes = [2]
    for num in range(3, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    right_truncatable = []
    for prime in primes:
        trunc = prime
        while trunc > 0:
            if trunc not in primes:
                break
            right_truncatable.append(trunc)
            trunc //= 10
    return sorted(list(set(right_truncatable)))