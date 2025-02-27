def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[88]
    rs = []
    for i in range(x, 1, -1):
        if is_prime(i):
            j = i
            while j > 1:
                if not is_prime(j):
                    break
                j //= 10
                if j == 0:
                    rs.append(i)
    return sorted(rs, reverse=True)