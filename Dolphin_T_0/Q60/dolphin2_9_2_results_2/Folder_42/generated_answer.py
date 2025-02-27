def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(n):
    d = list(map(int, str(n)))
    d.reverse()
    res = []
    for x in range(10 ** (len(d) - 1), 10 ** len(d)):
        if is_prime(x):
            d1 = list(map(int, str(x)))
            if 0 in d1:
                continue
            d1.reverse()
            flag = 1
            while len(d1) > 1:
                d1.pop()
                if not is_prime(int(''.join(map(str, d1[::-1])))):
                    flag = 0
                    break
            if flag:
                res.append(x)
    return list(reversed(res))