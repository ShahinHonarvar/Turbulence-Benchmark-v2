def all_right_truncatable_prime(tup):
    x = tup[70]
    result = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable(i):
            result.append(i)
    result.sort(reverse=True)
    return result

def is_prime(i):
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            return False
    return True

def is_right_truncatable(i):
    num = i
    while num > 9:
        num = num // 10
        if not is_prime(num):
            return False
    return True