def all_left_right_truncatable_prime(t):
    x = t[46]
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and (not '0' in str(i))]
    trunc_primes = [i for i in primes if all((int(''.join(str(i)[j:i - j])) in primes for j in range(1, len(str(i)) - 1)))]
    return sorted(trunc_primes, reverse=True)