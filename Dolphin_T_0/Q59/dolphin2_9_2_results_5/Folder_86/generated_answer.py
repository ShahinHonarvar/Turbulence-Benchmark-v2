def all_left_truncatable_prime(t):
    x = t[126]
    primes = [2, 3, 5, 7]
    for i in range(10, x + 1):
        if isprime(i):
            for j in range(len(str(i)) - 1):
                if isprime(int(str(i)[j:])):
                    if j == len(str(i)) - 2:
                        primes.append(i)
                else:
                    break
    return sorted(primes, reverse=True)

def isprime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True