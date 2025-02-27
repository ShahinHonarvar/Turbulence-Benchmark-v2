def all_right_truncatable_prime(t):
    a = []
    x = t[81]
    for i in range(2, x):
        if is_prime(i) and is_truncatable(i):
            a.append(i)
    return sorted(a, reverse=True)

def is_prime(i):
    if i == 2:
        return True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def is_truncatable(i):
    a = str(i)
    for j in range(1, len(a)):
        if not is_prime(int(a[:-j])):
            return False
    return True