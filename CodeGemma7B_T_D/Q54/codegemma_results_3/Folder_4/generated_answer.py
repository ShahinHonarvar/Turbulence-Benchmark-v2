def all_right_truncatable_prime(t):
    x = t[96]
    n = x - 1
    result = []
    while n > 2:
        if prime(n) and right_truncatable(n):
            result.append(n)
        n -= 2
    return sorted(result, reverse=True)

def right_truncatable(n):
    a = str(n)[::-1]
    for i in range(1, len(a)):
        if not prime(int(a[:i])):
            return False
    return True

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True