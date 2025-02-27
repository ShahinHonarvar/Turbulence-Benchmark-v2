def all_left_right_truncatable_prime(t):
    x = t[86]
    ans = []
    for i in range(2, x):
        f = True
        if '0' in str(i):
            continue
        for j in range(1, len(str(i)) // 2 + 1):
            left = int(str(i)[:j])
            right = int(str(i)[-j:])
            if not is_prime(left) or not is_prime(right):
                f = False
                break
        if f:
            ans.append(i)
    return sorted(ans, reverse=True) if ans else ans

def is_prime(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True