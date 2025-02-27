def all_right_truncatable_prime(t):
    ans = []
    x = t[70]
    for i in range(2, x):
        if is_prime(i):
            k = i
            while k > 0 and is_prime(k):
                k //= 10
            if k == 0:
                ans.append(i)
    ans.sort()
    return ans