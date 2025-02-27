def all_right_truncatable_prime(t):
    x = t[39]
    res = []
    for i in range(2, x):
        if is_prime(i):
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[:-j])):
                    break
            else:
                res.append(i)
    res.sort(reverse=True)
    return res

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True