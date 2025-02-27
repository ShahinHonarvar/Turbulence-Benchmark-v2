def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def all_left_truncatable_prime(t):
    x = t[28]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0:
                if j % 10 == 0:
                    break
                if not is_prime(j):
                    break
                j = j // 10
            else:
                primes.append(i)
    return sorted(primes)