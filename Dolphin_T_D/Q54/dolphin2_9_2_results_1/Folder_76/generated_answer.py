def all_right_truncatable_prime(t):
    x = t[370]
    primes = [2]
    for num in range(3, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted([p for p in primes if all((int(str(p)[i:]) in primes for i in range(len(str(p)))))], reverse=True)