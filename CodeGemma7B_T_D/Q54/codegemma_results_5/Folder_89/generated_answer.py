from math import sqrt, ceil

def all_right_truncatable_prime(tup):
    x = tup[97]
    ans = []
    for i in range(x - 2, 2, -1):
        if is_prime(i):
            j = i
            ok = True
            while j:
                if not is_prime(j):
                    ok = False
                    break
                j //= 10
            if ok:
                ans.append(i)
    ans.sort(reverse=True)
    return ans

def is_prime(x):
    if x <= 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True