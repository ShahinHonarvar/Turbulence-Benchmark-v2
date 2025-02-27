def all_right_truncatable_prime(t):
    x = t[79]
    k = 2
    c = set()
    while k < x:
        if is_prime(k):
            while k % 10 != 0 and all_right_truncatable(k):
                c.add(k)
                k += 2 if k % 2 == 0 else 3
        else:
            k += 2 if k % 2 == 0 else 3
    return sorted(list(c), reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable(k):
    while k != 0:
        if not is_prime(k):
            return False
        k //= 10
    return True