def all_left_truncatable_prime(l):
    x = l[26]
    res = []
    for i in range(2, x):
        if all_left_truncatable_prime_check(i):
            res.append(i)
    return sorted(res)

def all_left_truncatable_prime_check(i):
    if i < 10:
        if is_prime(i):
            return True
        else:
            return False
    elif i % 10 == 0:
        return False
    elif is_prime(i):
        return all_left_truncatable_prime_check(i // 10)
    else:
        return False

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True