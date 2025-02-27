def all_left_truncatable_prime(tup):
    x = tup[433]
    res = []
    for i in range(2, x):
        if isprime(i) and (not has_zero(i)) and is_left_truncatable(i):
            res.append(i)
    res.sort(reverse=True)
    return res

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def has_zero(num):
    return '0' in str(num)

def is_left_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not isprime(int(str_num[i:])):
            return False
    return True