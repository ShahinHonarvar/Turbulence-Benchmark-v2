def all_right_truncatable_prime(num):
    primes = [i for i in range(2, num + 1) if all((j % i != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_primes = []
    for prime in primes:
        temp = prime
        while temp > 0:
            if temp in primes:
                right_truncatable_primes.append(temp)
            temp //= 10
    return sorted(right_truncatable_primes, reverse=True)