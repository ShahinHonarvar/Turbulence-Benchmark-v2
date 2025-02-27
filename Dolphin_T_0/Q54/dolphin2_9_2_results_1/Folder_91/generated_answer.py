def right_trunc(num):
    while True:
        yield num
        num //= 10

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[0]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            for num in right_trunc(i):
                if not is_prime(num):
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)