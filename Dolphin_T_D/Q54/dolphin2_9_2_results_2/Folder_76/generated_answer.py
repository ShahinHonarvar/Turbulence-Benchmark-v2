def all_right_truncatable_prime(t):
    x = t[370]
    r = []
    for i in range(2, x):
        if all([i % int(str(i)[j:]) != 0 for j in range(len(str(i))) if len(str(i)) - j > 0]):
            r.append(i)
    return sorted(r, reverse=True) or []