def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(a):
    x = a[39]
    primes = [2, 3]
    for n in range(4, x):
        if is_prime(n):
            m = n
            while m != 0:
                if not is_prime(m):
                    break
                m //= 10
            else:
                primes.append(n)
    return sorted(primes, reverse=True)