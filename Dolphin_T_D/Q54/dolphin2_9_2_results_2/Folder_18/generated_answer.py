def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[429]
    r = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j:
                if j != i and is_prime(j):
                    r.append(i)
                    break
                j //= 10
    return sorted(r, reverse=True)