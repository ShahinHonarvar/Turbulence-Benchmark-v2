def all_left_truncatable_prime(t):
    x = t[49]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            if all((int(str(num)[i:]) in primes for i in range(1, len(str(num))))):
                primes.append(num)
    return sorted(primes)