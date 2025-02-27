def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def all_left_right_truncatable_prime(numbers):
    x, = numbers
    primes = []
    for n in range(2, x + 1):
        if is_prime(n) and (not '0' in str(n)):
            trunc = n
            while trunc >= 10:
                trunc = int(str(trunc)[1:-1])
                if not is_prime(trunc):
                    break
            else:
                primes.append(n)
    primes.sort()
    return primes