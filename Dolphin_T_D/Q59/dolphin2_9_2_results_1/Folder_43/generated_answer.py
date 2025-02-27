def is_truncatable_prime(n):
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[89]
    ans = []
    for n in range(x, 1, -1):
        if is_truncatable_prime(n):
            ans.append(n)
    return ans