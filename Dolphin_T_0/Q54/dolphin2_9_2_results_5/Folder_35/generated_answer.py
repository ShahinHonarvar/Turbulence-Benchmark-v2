def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[177]
    res = []
    for i in range(2, x):
        if is_prime(i):
            n = i
            flag = True
            while n != 0:
                if not is_prime(n):
                    flag = False
                    break
                n //= 10
            if flag:
                res.append(i)
    return sorted(res)