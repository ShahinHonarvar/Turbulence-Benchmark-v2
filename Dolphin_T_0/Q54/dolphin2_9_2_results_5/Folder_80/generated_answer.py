def is_prime(n):
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

def all_right_truncatable_prime(t):
    x = t[14]
    primes = [2]
    i = 3
    while i < x:
        if is_prime(i):
            primes.append(i)
            n = i
            while n:
                n //= 10
                if n < 10 or is_prime(n):
                    continue
                else:
                    i += 2
                    break
            else:
                i += 2
        else:
            i += 2
    primes.sort(reverse=True)
    return primes