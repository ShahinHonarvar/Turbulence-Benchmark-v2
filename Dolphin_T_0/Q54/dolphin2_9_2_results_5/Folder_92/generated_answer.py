def all_right_truncatable_prime(t):
    x = t[7]
    primes = [2, 3, 5, 7]
    for num in range(8, x):
        if all((num % i != 0 for i in range(2, num))):
            if all((int(str(num)[:-i]) in primes for i in range(1, len(str(num))))):
                primes.append(num)
    return sorted(primes)