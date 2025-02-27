def all_left_truncatable_prime(tup):
    ans = []
    x = tup[14]
    for c in range(2, x):
        n = c
        t = True
        for i in range(1, len(str(c))):
            n = int(str(n)[1:])
            if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or (n % 7 == 0) or (n not in ans):
                t = False
                break
        if t:
            ans.append(c)
    ans.sort(reverse=True)
    return ans