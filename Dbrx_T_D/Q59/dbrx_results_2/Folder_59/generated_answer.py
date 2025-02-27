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
    for i in range(10, n):
        if is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j = j // 10
            if j == 0:
                result.append(i)
    return sorted(result, reverse=True)