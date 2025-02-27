def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[29]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc = int(str(trunc)[:-1])
                if trunc == 0:
                    primes.append(i)
                    break
    return primes