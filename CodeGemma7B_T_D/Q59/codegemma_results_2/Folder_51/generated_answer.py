def all_left_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if is_prime(i) and (not has_zero(i)):
            if is_left_truncatable(i):
                result.append(i)
    return sorted(result)

def is_prime(i):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def has_zero(i):
    while i > 0:
        if i % 10 == 0:
            return True
        i //= 10
    return False

def is_left_truncatable(i):
    temp = i
    while temp > 0:
        if not is_prime(temp):
            return False
        temp //= 10
    return True