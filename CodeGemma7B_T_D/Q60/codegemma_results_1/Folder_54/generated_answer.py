def left_truncatable_prime(n):
    for i in range(n):
        if is_prime(i) and (not has_zero(i)) and is_prime(i // 10 ** (len(str(i)) - 1)):
            return True
    return False

def right_truncatable_prime(n):
    for i in range(n):
        if is_prime(i) and (not has_zero(i)):
            if is_prime(i):
                for j in range(len(str(i))):
                    if not is_prime(i // 10 ** (j + 1)):
                        break
                    i //= 10 ** (j + 1)
            else:
                continue
            return True
    return False

def all_left_right_truncatable_prime(tup):
    x = tup[88]
    res = []
    for i in range(x + 1):
        if left_truncatable_prime(i) and right_truncatable_prime(i):
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
    return 0 in map(int, str(n))