def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(lst):
    x = lst[54]
    primes = [i for i in range(2, x) if is_prime(i)]
    while len(primes) > 0:
        for i in range(len(primes) - 1, -1, -1):
            if not is_prime(int(primes[i] / 10)):
                del primes[i]
    return primes[::-1]