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

def all_left_truncatable_prime(t):
    x = t[100]
    primes = [2, 3, 5, 7]
    for n in range(11, x):
        if '0' in str(n):
            continue
        if is_prime(n):
            k = n
            while k > 0:
                if not is_prime(k):
                    break
                k = int(k / 10)
                if k == 0:
                    primes.append(n)
                    break
    return sorted(primes)