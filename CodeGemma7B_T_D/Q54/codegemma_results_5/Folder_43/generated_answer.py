def all_right_truncatable_prime(a):
    x = a[89]
    prime = [True] * (2 * 10 ** 5 + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(2 * 10 ** 5 + 0.5)):
        if prime[i]:
            for j in range(i * i, 2 * 10 ** 5 + 1, i):
                prime[j] = False
    for i in range(x - 1, 9, -1):
        b = str(i)
        for j in range(1, len(b)):
            if not prime[int(b[j:])]:
                break
        else:
            yield i