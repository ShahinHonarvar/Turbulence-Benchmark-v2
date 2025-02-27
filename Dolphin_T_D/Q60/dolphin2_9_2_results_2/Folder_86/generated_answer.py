def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    m = int(str(n)[1:-1])
    return is_prime(m) and is_truncatable_prime(m)

def all_left_right_truncatable_prime(t):
    l = []
    x = t[126]
    for i in range(2, x + 1):
        if str(i).count('0') == 0 and is_truncatable_prime(i):
            l.append(i)
    l.sort(reverse=True)
    return l