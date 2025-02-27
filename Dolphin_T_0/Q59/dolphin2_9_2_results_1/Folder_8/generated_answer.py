def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[41]
    ret = []
    for i in range(x - 1, 1, -1):
        if is_prime(i) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i))))):
            ret.append(i)
    return ret