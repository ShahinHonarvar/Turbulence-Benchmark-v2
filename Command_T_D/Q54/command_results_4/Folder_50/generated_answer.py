def all_right_truncatable_prime(x):
    return [str(n) for n in set(range(2, x // 10 + 1)) if all((n % d for d in range(3, int(str(n)[-1]) + 1, 2)))]