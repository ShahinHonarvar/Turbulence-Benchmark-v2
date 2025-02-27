def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[94]
    res = []
    for i in range(2, x):
        s = str(i)
        if '0' not in s:
            j = 0
            while j < len(s):
                if all((is_prime(int(s[j:]) + 10 ** k) for k in range(j + 1))):
                    j += 1
                else:
                    break
            if j == len(s):
                res.append(i)
    return res