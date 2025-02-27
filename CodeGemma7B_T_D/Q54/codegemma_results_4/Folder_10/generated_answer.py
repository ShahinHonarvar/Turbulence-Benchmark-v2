def all_right_truncatable_prime(t):
    x = t[38]
    ans = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable(i, x):
            ans.append(i)
    return sorted(ans, reverse=True)

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_right_truncatable(x, max_num):
    for i in range(1, len(str(x))):
        num = int(str(x)[:-i])
        if not is_prime(num) or num >= max_num:
            return False
    return True