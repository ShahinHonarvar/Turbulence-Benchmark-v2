def all_right_truncatable_prime(tup):
    x = tup[81]
    res = []
    for i in range(x - 1, 1, -1):
        if is_prime(i) and right_truncatable(i):
            res.append(i)
    res.sort(reverse=True)
    return res

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable(num):
    rem = num % 10
    while num:
        num //= 10
        if (rem == 2 or rem == 3 or rem == 5 or (rem == 7)) and (not is_prime(num)):
            return False
        rem = num % 10
    return True