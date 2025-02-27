def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    str_n = str(n)
    l = []
    for i in range(1, len(str_n)):
        if is_prime(int(str_n[:-i])):
            l.append(int(str_n[:-i]))
    return sorted(l, reverse=True)

def all_right_truncatable_prime(x):
    return right_truncatable_prime(x[50])