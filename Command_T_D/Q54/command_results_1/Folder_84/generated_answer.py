def all_right_truncatable_prime(x):
    return [n for n in range(x, 2, -1) if all((n % d == 0 for d in range(2, int(str(n)[-1]) + 1) if n % d == 0))]