def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    result = []
    for i in range(1, t[61]):
        if is_prime(i):
            j = i
            while j != 0:
                j //= 10
                if is_prime(j):
                    result.append(i)
    return sorted(list(set(result)))