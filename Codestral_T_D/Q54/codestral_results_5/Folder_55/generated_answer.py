def all_right_truncatable_prime(t):
    x = t[73]
    primes = [i for i in range(2, x) if all((int(str(i)[:j]) > 1 for j in range(1, len(str(i)) + 1)))]
    return sorted([i for i in primes if all((int(str(i)[:j]) in primes for j in range(1, len(str(i)))))], reverse=True)