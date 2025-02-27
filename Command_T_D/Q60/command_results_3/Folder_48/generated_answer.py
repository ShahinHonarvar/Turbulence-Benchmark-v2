def all_left_right_truncatable_prime(n):
    if not n:
        return []
    s = str(min(n))
    l = s[:2] + s[2:]
    r = l[-2:] + l[-1] + l[-2:-1] + l[-3:-2]
    for i in range(2, int(s[1:]) + 1):
        if all((l[j] == r[i - j - 1] for j in range(i, min(i + 10, len(l))))):
            yield int(s[:i] + l[i:j] + l[j + 1:])
    for i in range(2, int(r[1:]) + 1):
        if all((l[j] == r[i - j - 1] for j in range(i, min(i + 10, len(r))))):
            yield int(l[:i] + l[i:j] + l[j + 1:])