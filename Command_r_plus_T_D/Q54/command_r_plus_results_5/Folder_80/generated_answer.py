def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(n):
    primes = []
    for i in range(10 ** n, 10 ** (n - 1) - 1, -1):
        if is_prime(i):
            truncated_prime = i
            while len(str(truncated_prime)) > 1:
                truncated_prime //= 10
                if not is_prime(truncated_prime):
                    break
            if len(str(truncated_prime)) == 1:
                primes.append(i)
    return primes

def all_right_truncatable_prime(tup):
    x = tup[14]
    primes = right_truncatable_primes(len(str(x)))
    primes = [p for p in primes if p < x]
    return sorted(primes, reverse=True)