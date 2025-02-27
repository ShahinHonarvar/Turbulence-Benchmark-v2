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

def left_truncatable_primes(n):
    result = []
    for i in range(1, 10):
        if is_prime(i):
            result.append(i)
    for i in range(1, 10):
        for j in result:
            num = i * 10 + j
            if is_prime(num):
                result.append(num)
    result = [x for x in result if x < n]
    result.sort(reverse=True)
    return result

def all_left_truncatable_prime(t):
    return left_truncatable_primes(t[3])