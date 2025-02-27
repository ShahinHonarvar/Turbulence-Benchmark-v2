def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[87]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num != 0:
                if is_prime(num):
                    num //= 10
                else:
                    break
            else:
                primes.append(i)
    return sorted(primes)