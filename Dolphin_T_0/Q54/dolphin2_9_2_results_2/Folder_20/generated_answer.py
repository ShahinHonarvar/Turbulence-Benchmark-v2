def is_prime(n):
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(t):
    x = t[100]
    l = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    break
            else:
                l.append(i)
    return l[::-1] or []