def all_left_truncatable_prime(t):
    left_truncatable = []
    x = t[26]
    for i in range(2, x):
        if is_prime(i) and (not str(i) == '0') and is_prime(int(str(i)[1:])):
            left_truncatable.append(i)
    return sorted(left_truncatable)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True