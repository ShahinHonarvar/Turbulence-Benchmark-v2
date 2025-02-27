from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[55]
    prime = [i for i in range(2, x) if is_prime(i)]
    return sorted([p for p in prime if all((is_prime(p // 10 ** i) for i in range(1, int(log10(p)))))], reverse=True)