def all_left_right_truncatable_prime(t):
    x = t[54]
    prime_check = lambda n: all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))
    truncatable_check = lambda n: all((int(str(n)[i + 1:] + str(n)[i]) % i != 0 for i in range(1, len(str(n)) - 1)))
    return sorted([n for n in range(11, x + 1) if prime_check(n) and truncatable_check(n)])