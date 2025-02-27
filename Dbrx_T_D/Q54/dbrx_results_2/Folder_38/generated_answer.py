def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def find_right_truncatable_primes(x):
    result = []
    for i in range(1, 10):
        num = i
        while num < x:
            if is_prime(num):
                result.append(num)
            num = num * 10 + i
    return sorted(result)

def all_right_truncatable_prime(t):
    x = t[28]
    return [i for i in find_right_truncatable_primes(x) if i < x]