def all_left_truncatable_prime(t):
    x = t[74]
    primes = [2]
    ltrunc_primes = []
    for num in range(3, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    for prime in primes:
        num = str(prime)
        if '0' not in num:
            ltrunc = [int(num[i:]) for i in range(len(num)) if int(num[i:]) in primes]
            if len(ltrunc) == len(num):
                ltrunc_primes.append(prime)
    return sorted(ltrunc_primes)