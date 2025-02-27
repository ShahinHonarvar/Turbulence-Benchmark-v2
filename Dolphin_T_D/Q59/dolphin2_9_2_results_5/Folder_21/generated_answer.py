def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[175]
    result = []
    for i in range(2, x):
        if is_prime(i) and i % 10 != 0:
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j //= 10
                if j == 0:
                    result.append(i)
    result.sort()
    return result