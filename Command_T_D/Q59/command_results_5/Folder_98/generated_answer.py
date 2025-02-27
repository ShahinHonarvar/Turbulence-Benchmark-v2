def all_left_truncatable_prime(x):
    return [n for n in range(2, x) if all((n % d for d in range(3, int(str(n)[0])))) and all((n % d == 0 for d in range(2, int(str(n)[0])))) and (n > 1)]