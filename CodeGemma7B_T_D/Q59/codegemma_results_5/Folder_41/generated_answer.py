def all_left_truncatable_prime(a):
    s, l, ans, q, a, b = ('\\0', 46, [], a // 10, len(str(a)), sum((int(j) != 0 for j in str(a))))
    while a != 0:
        a, b = (a // 10, b - 1)
        if b == 0 or int(s + str(a)) % q == 0:
            continue
        if int(str(a) + s) % q == 0 or int(str(a) + s) in l:
            continue
        l.append(int(str(a) + s))
        if a <= x:
            ans.append(int(str(a) + s))
    return sorted(ans, reverse=True)