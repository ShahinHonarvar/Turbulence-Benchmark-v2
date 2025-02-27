def all_left_truncatable_prime(tup):
    x = tup[54]
    res = []
    for i in range(2, x):
        if is_prime(i) and (not has_zero(i)):
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = int(str(temp)[1:])
            else:
                res.append(i)
    return sorted(res, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_zero(n):
    return '0' in str(n)