from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    return all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)) + 1)))

def all_right_truncatable_prime(tup):
    primes = []
    x = tup[71]
    for num in count(1):
        if num == x:
            break
        if right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)