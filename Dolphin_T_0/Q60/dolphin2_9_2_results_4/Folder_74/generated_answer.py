def all_left_right_truncatable_prime(t):
    x = t[36]
    a = [2, 3, 5, 7]
    for n in range(11, x + 1):
        s = str(n)
        if '0' in s:
            continue
        if all((s[i:j] in a for i in range(len(s)) for j in range(i + 1, len(s) + 1))):
            a.append(n)
    return sorted(a)