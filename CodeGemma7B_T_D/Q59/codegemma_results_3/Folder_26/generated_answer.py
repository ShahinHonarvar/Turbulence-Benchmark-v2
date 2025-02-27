def all_left_truncatable_prime(t):
    x = t[81]
    p = set((i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))))
    ans = []
    for n in range(x - 1, 1, -1):
        if n not in p:
            continue
        for k in range(int(str(n)[::-1])):
            if k == 0 or str(n).startswith(str(k)):
                if n in p and int(''.join(str(n)[k:])) in p:
                    ans.append(n)
                    break
    ans.sort()
    return ans