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

def trunc(n):
    if n <= 0:
        return False
    n = str(n)
    for i in range(len(n) - 1):
        if not is_prime(int(n[i:])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[85]
    l = [i for i in range(x) if trunc(i) and is_prime(i)]
    return sorted(l)