def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(t):
    x = t[803]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            n = num
            while n > 0:
                if not is_prime(n):
                    break
                if n != 0:
                    n = int(str(n)[1:])
            else:
                primes.append(num)
    return sorted(primes)