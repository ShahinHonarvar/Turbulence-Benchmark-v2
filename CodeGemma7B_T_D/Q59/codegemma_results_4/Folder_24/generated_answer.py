def all_left_truncatable_prime(a):
    x = a[65]
    v = []
    for i in range(2, x):
        if all((digit not in str(i) for digit in '0')):
            u = i
            while u >= 10:
                if not is_prime(u):
                    break
                u //= 10
            if u >= 10:
                continue
            v.append(i)
    return sorted(v, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True