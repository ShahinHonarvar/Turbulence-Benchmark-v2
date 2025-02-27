def all_right_truncatable_prime(t):
    x = t[81]
    primes = [2, 3, 5, 7]
    for i in range(11, x, 2):
        if all((int(str(i)[-j]) % 2 != 0 for j in range(1, len(str(i))) if j != len(str(i)) - 1 or j != 1)):
            primes.append(i)
    return [p for p in primes if all((int(p[i:j]) != 1 for i in range(len(p)) and j in range(i, len(p)))) and all((int(p[i:]) % p == 0 for i in range(len(p))))]