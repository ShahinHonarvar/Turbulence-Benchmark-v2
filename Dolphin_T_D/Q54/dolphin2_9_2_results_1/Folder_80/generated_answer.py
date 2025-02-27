def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_last_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(t):
    x = t[14]
    res = []
    for val in range(x, 1, -1):
        if is_prime(val):
            k = val
            while k != 0 and is_prime(k):
                k = remove_last_digit(k)
            if k == 0:
                res.append(val)
    return res[::-1]