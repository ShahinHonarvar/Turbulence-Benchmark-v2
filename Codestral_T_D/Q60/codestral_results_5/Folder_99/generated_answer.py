def all_left_right_truncatable_prime(t):
    x = t[758]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            s = str(num)
            if '0' not in s and all((int(s[i:]) in primes for i in range(1, len(s)))):
                primes.append(num)
    return sorted(primes)