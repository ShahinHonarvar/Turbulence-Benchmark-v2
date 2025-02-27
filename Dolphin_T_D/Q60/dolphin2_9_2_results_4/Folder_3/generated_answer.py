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

def all_left_right_truncatable_prime(t):
    x = t[100]
    primes = [2]
    for i in range(3, x + 1):
        if is_prime(i):
            if all(is_prime(int(str(i)[1:-1]))):
                primes.append(i)
    return primes