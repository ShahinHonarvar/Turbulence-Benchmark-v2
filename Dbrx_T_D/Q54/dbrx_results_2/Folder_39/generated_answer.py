def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 2
    return True

def right_truncatable_prime(n):
    while True:
        if is_prime(n):
            yield n
        if n % 10 == 1:
            break
        n //= 10

def all_right_truncatable_prime(t):
    x = t[29]
    rtp = []
    for i in right_truncatable_prime(x):
        rtp.append(i)
    rtp.sort(reverse=True)
    return rtp