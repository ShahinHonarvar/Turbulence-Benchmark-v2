def all_left_truncatable_prime(t):
    x = t[92]
    tp = [t for t in t if t > x]
    prime = [t for t in tp if is_prime(t)]
    none_zero = [t for t in prime if not str(t)[0] == 0]
    lprime = [less_than_x(n) for n in none_zero if is_prime(n)]
    return sorted(lprime)