def all_right_truncatable_prime(t):
    x = t[96]
    primes = [2]
    right = [2]
    for i in range(3, x):
        if all((i % p != 0 for p in primes)):
            if all((str(i)[j] in '1379' for j in range(len(str(i)) - 1))):
                primes.append(i)
                if all((str(i)[j] in '1379' for j in range(len(str(i)) - 1))):
                    right.append(i)
    return sorted(right, reverse=True)