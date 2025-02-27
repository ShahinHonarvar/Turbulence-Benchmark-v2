def all_right_truncatable_prime(t):
    x = t[784]
    primes = []
    for num in range(2, x):
        temp = num
        while temp > 0:
            if temp not in primes:
                break
            temp //= 10
        else:
            primes.append(num)
    right_truncatable_primes = []
    for prime in primes:
        temp = prime
        while temp > 0:
            if temp not in primes:
                break
            temp //= 10
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)