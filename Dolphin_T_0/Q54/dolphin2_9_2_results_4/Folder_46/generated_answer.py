def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[33]
    rs = []
    for i in range(1, x):
        j = i
        while j != 0 and is_prime(j):
            rs.append(j)
            j //= 10
    rs.sort()
    return rs