def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[29]
    primes = [2]
    n = 3
    while n < x:
        if n % 2 != 0 and all((isPrime(int(''.join(str(n)[i:]))) for i in range(1, len(str(n))))):
            primes.append(n)
        n += 1
    return sorted(primes, reverse=True)