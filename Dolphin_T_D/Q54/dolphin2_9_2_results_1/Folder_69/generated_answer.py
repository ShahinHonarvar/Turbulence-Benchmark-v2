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

def all_right_truncatable_prime(t):
    x = t[760]
    primes = [2, 3, 5, 7]
    for n in range(11, x):
        if is_prime(n):
            for i in range(len(str(n)) - 1, 0, -1):
                if not is_prime(int(str(n)[i:])):
                    break
                primes.append(n)
    return sorted(primes, reverse=True)