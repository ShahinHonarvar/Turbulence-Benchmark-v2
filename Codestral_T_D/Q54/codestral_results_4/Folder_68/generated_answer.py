def all_right_truncatable_prime(t):
    x = t[1]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and all((i % int(f'1{i[1:]}') == 0 for i in str(i)[1:])):
            primes.append(i)
    return sorted(primes, reverse=True)