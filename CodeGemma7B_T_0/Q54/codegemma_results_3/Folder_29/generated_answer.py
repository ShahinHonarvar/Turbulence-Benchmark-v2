def all_right_truncatable_prime(t):
    x = t[55]
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

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True