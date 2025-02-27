def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[89]
    res = [i for i in range(x, 0, -1) if is_prime(i)]
    for i in range(len(res) - 1, -1, -1):
        if any((int(str(res[i])[1:]) != res[j] for j in range(i))):
            res.pop(i)
    return res