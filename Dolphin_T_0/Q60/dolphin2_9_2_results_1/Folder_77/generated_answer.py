def all_left_right_truncatable_prime(n):
    x = n[767]
    primes = []
    for i in range(11, x + 1):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            str_i = str(i)
            if '0' not in str_i and all((str(int(str_i[1:-1])) in primes for _ in range(1, len(str_i) - 1))):
                primes.append(str(i))
    return sorted(primes, key=lambda p: int(p), reverse=True)