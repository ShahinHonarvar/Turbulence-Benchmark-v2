def all_left_truncatable_prime(tup):
    x = tup[52]
    res = []
    for i in range(2, x):
        if is_prime(i) and (not has_zero(i)):
            tmp = i
            while tmp > 0:
                if not is_prime(tmp):
                    break
                tmp = int(str(tmp)[1:])
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

def has_zero(n):
    return '0' in str(n)