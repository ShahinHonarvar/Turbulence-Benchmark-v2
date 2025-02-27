def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[792]
    rtp = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0 and is_prime(j):
                j //= 10
            if j == 0:
                rtp.append(i)
    return sorted(rtp)