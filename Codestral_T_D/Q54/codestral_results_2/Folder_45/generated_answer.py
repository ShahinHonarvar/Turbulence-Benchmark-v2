def all_right_truncatable_prime(t):
    x = t[61]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            trunc = num
            while trunc > 0:
                if trunc not in primes:
                    break
                trunc = trunc // 10
            else:
                primes.append(num)
    return sorted(primes)