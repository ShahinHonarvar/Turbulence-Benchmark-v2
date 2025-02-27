def all_left_truncatable_prime(t):
    x = t[36]
    L = [a for a in range(2, x) if '0' not in str(a) and all((b in s for b in str(a) for s in [str(a)]))]
    return sorted(L, reverse=True)