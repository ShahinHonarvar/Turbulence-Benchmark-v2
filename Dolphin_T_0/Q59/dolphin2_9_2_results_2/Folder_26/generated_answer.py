def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(a):
    x = a[0]
    return sorted([i for i in range(x, 0, -1) if all((is_prime(int(str(i)[j:])) for j in range(len(str(i)))))], reverse=True)