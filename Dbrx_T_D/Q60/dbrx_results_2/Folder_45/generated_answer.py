def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[60]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    result = []
    for prime in primes:
        digits = len(str(prime))
        for i in range(1, digits):
            if not is_prime(int(str(prime)[i:])):
                break
            if not is_prime(int(str(prime)[:-i])):
                break
        else:
            result.append(prime)
    return sorted(result)