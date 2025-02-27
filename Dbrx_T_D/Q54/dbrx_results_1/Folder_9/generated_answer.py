import itertools

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[29]
    result = []
    for i in itertools.count(1):
        if not is_prime(i):
            continue
        s = str(i)
        for j in range(1, len(s)):
            if not is_prime(int(s[j:])):
                break
        else:
            result.append(i)
        if i >= x:
            break
    return sorted(result, reverse=True)