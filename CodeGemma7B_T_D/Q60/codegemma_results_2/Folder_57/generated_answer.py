def is_prime(x):
    x = abs(x)
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 2):
        if x % i == 0:
            return False
    return True

def lefttrunc(x):
    x = str(x)
    for i in range(1, len(x)):
        x = x[i:]
        if not is_prime(int(x)):
            return False
    return True

def righttrunc(x):
    x = str(x)
    for i in range(len(x), 1, -1):
        x = x[:i]
        if not is_prime(int(x)):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[54]
    ans = []
    for i in range(x, 0, -1):
        if str(i) != str(i)[::-1] and '0' not in str(i):
            if lefttrunc(i) and righttrunc(i):
                ans.append(i)
    return sorted(ans, reverse=True)