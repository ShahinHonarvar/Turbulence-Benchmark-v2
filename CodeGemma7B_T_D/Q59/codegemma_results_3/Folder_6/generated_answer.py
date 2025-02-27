def all_left_truncatable_prime(t):
    l = [i for i in t if str(i) not in '0']
    ans = []
    for k in l:
        i = k
        f = True
        while i > 0 and f:
            i //= 10
            if i in l and i != k:
                f = False
        if f:
            ans.append(k)
    return sorted(ans)