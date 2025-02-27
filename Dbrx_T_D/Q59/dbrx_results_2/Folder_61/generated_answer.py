def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(x):
    primes = []
    for i in range(1, 10):
        if is_prime(i):
            for j in range(1, len(str(x))):
                num = int(str(i) + '0' * j + str(x)[j:])
                if is_prime(num):
                    primes.append(num)
    return sorted(list(set(primes)), reverse=True)