def all_right_truncatable_prime(t):
    x = t[100]
    primes = [2]
    send = [1]
    if x < 2:
        return []
    for n in range(3, x, 2):
        if all((n % p != 0 for p in primes)):
            primes.append(n)
            send.append(1)
        else:
            send.append(0)
    return sorted([n for n in primes if send[-n:] == [1, 1]], reverse=True)