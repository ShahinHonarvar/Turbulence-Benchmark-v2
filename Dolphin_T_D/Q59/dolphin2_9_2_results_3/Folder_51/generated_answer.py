def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[54]
    primes = []
    i = 2
    while i < x:
        if is_prime(i):
            trunc = i
            while trunc != 0:
                if not is_prime(trunc):
                    break
                trunc = int(trunc / 10)
            if trunc == 0:
                primes.append(i)
        i += 1
    return sorted(primes)