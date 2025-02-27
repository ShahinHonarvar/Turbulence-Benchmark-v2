def right_truncatable(num):
    if num < 2:
        return False
    while num != 0:
        if num % 2 == 0 and num != 2:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        num //= 10
    return True

def all_right_truncatable_prime(tup):
    x = tup[175]
    primes = [i for i in range(2, x) if right_truncatable(i)]
    primes.sort()
    return primes