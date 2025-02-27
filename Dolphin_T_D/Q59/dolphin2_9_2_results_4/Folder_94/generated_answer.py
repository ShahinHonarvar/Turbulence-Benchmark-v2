def all_left_truncatable_prime(tq):
    x = tq[43]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            if all((primes and int(str(pr).replace(str(num)[-1], '')) % pr != 0 for pr in primes)):
                if all((primes and num % int(num % 10 ** i + 10 ** i, num != int(num % 10 ** i + 10 ** i)) for i in range(1, len(str(num))))):
                    primes.append(num)
    return sorted(primes)