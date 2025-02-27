def all_left_truncatable_prime(x):
    x = x[945]
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    left = []
    for p in range(2, int(x ** 0.5 + 1)):
        if prime[p]:
            if not any((int(str(p)[:i]) % p for i in range(2, len(str(p))))):
                left.append(p)
            for i in range(p * 2, x + 1, p):
                prime[i] = False
    return sorted(left, reverse=True)