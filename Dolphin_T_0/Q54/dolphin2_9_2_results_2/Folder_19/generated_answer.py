def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(t):
    x = t[67]
    primes = []
    for num in range(x - 1, 0, -1):
        if is_prime(num):
            r = num
            while r > 0:
                if not is_prime(r):
                    break
                r //= 10
                if r == 0:
                    primes.append(num)
                else:
                    break
    return sorted(primes, reverse=True)