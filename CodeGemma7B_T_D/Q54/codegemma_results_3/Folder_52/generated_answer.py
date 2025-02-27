def all_right_truncatable_prime(z):
    x = z[52]
    a = []
    for n in range(2, x):
        if prime(n):
            for i in range(1, len(str(n))):
                if prime(int(str(n)[:-i])):
                    a.append(n)
                else:
                    break
    return sorted(a)[::-1] if a else []