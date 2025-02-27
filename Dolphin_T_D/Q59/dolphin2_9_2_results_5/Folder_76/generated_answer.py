def all_left_truncatable_prime(t):
    x = t[370]
    L = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 1:
                if not is_prime(j):
                    break
                j //= 10
            if j == 1:
                L.append(i)
    L.sort(reverse=True)
    return L

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True