def all_left_truncatable_prime(tup):
    x = tup[77]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, num))):
            s = str(num)
            if '0' not in s:
                if all((int(s[i:]) in primes for i in range(1, len(s)))):
                    primes.append(num)
    return sorted(primes)