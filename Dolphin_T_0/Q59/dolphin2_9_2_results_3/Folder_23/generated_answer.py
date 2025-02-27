def all_left_truncatable_prime(t):
    x = t[77]
    prime = []
    for n in range(2, x):
        if all((n % d != 0 for d in range(2, int(n ** 0.5) + 1))):
            if all(int((''.join(s[n:]) for n in range(1, len(''.join(map(str, prime)))))) not in [0] and all((s[n] in prime for n in range(len(''.join(map(str, prime))))))):
                prime.append(n)
    return sorted(prime, reverse=True)