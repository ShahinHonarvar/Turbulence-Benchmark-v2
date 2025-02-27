def all_left_right_truncatable_prime(t):
    x = t[98]
    primes = [2]
    for num in range(3, x + 1, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)

    def is_truncatable(p):
        s = str(p)
        return all((int(s[i:]) in primes and int(s[:-i]) in primes for i in range(1, len(s))))
    return sorted(filter(is_truncatable, primes))