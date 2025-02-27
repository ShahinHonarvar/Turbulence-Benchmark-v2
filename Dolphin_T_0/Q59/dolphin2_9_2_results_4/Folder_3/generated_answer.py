def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
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
    x = t[100]
    ltp = []
    if x > 1:
        ltp.append(2)
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            i = n
            while i > 0:
                if not is_prime(i):
                    break
                i //= 10
            if i == 0:
                ltp.append(n)
    return ltp[::-1]