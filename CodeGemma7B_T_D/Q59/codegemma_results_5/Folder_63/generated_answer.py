def all_left_truncatable_prime(x):
    p = [n for n in range(2, x) if all((n % j != 0 for j in range(2, int(n ** 0.5) + 1)))]
    ans = []
    for n in p:
        s = str(n)
        if '0' in s:
            continue
        if all((int(s[i:]) % int(s[i + 1:]) != 0 for i in range(len(s) - 1))):
            ans.append(n)
    return sorted(ans)