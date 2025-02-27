def all_left_right_truncatable_prime(t):
    x = t[28]
    primes = [2, 3, 5, 7]
    for n in range(11, x + 1):
        if all(('0' not in str(n // i) and n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
            m = str(n)
            primes.append(int(m))
            for k in range(len(m) - 2):
                m = m[1:-1]
                if m[0] != '0' and int(m) in primes:
                    primes.append(int(m))
    return sorted(list(set(primes)))