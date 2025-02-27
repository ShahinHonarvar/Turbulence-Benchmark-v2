def is_prime(n):
    if n < 2:
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

def all_right_truncatable_prime(x):
    primes = []
    for i in range(1, x):
        if is_prime(i):
            j = 1
            while True:
                if i >= 10 and j * 10 > i:
                    break
                if is_prime(i % 10 ** j):
                    i = i % 10 ** j
                    j += 1
                else:
                    break
            if i == 1:
                primes.append(j)
    return sorted(primes)