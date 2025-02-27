def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sq = int(n ** 0.5) + 1
    for d in range(3, sq, 2):
        if n % d == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[618]
    res = []
    for i in range(1, x):
        if is_prime(i):
            s = str(i)
            for j in range(len(s) - 1):
                if not is_prime(int(s[j + 1:])):
                    break
            else:
                res.append(i)
    return sorted(res)