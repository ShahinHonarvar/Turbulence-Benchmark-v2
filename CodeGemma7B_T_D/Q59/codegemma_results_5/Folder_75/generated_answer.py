def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[41]
    result = []
    for i in range(2, x):
        if is_prime(i) and (not str(i).startswith('0')) and all_truncatable(i):
            result.append(i)
    return sorted(result)

def all_truncatable(n):
    num = str(n)
    for i in range(1, len(num)):
        if not is_prime(int(num[i:])):
            return False
    return True