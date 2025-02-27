def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[69]
    return sorted([i for i in range(x, 0, -1) if is_prime(i) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))))], reverse=True)