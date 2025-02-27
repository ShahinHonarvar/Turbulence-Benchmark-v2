def all_right_truncatable_prime(tp):
    x = tp[945]
    res = []
    for i in range(2, x):
        if is_prime(i):
            n = new_number(str(i))
            while n:
                if not is_prime(n):
                    break
                n = n // 10
            else:
                res.append(i)
    return sorted(res, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def new_number(s):
    return int(s[1:]) if s != '0' else None