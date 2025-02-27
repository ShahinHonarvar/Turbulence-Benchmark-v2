def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    p = 3
    while p * p <= n and n % p != 0:
        p += 2
    return p * p > n

def all_left_truncatable_prime(args):
    x = args[54]
    primes = [2]
    for n in range(3, x, 2):
        if is_prime(n):
            if all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n))))):
                primes.append(n)
    return primes