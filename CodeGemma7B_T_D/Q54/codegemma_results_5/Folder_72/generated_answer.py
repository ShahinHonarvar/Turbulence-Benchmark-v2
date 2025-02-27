from functools import cmp_to_key

def good(x):
    return x < 3 or x % 2 != 0

def prime(x):
    return x > 1 and (not any((x % i == 0 for i in range(3, int(x ** 0.5) + 1, 2))))

def left(m, k):
    if len(str(m)) <= k:
        return int(str(m))
    else:
        return int(str(m)[:-k])

def right(m, k):
    if len(str(m)) <= k:
        return int(str(m))
    else:
        return int(str(m)[-k:])

def all_right_truncatable_prime(t):
    x = t[31]
    list = []
    for num in range(2, x):
        if t[31] % right(num, 1) == 0:
            for i in range(2, len(str(num))):
                if len(str(num)) > 1:
                    num = left(num, 1)
                    if not prime(num):
                        break
                    elif t[31] % right(num, i) == 0 and (num in list or num == len(str(num))) and prime(num):
                        list.append(num)
    return sorted(list, cmp=cmp_to_key(reversed))