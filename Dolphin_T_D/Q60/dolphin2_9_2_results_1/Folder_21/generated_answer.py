def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[175]
    res = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            while len(s) > 1:
                if is_prime(int(s[1:len(s) - 1])):
                    s = s[1:len(s) - 1]
                else:
                    break
                if is_prime(int(s)):
                    res.append(i)
                else:
                    break
    return sorted(res)