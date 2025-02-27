def isprime(n):
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

def left_truncatable_primes():
    primes = [2, 3, 5, 7]
    for n in range(11, 10000000, 2):
        if isprime(n):
            flag = True
            for k in range(len(str(n))):
                if not isprime(int(str(n)[k:])):
                    flag = False
                    break
            if flag:
                primes.append(n)
    return primes

def all_left_truncatable_prime(t):
    x = t[23]
    ltp = left_truncatable_primes()
    return [p for p in ltp if p < x]