def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    max_prime = 29
    while primes[-1] < 10 ** 7:
        max_prime += 2
        if is_prime(max_prime):
            primes.append(max_prime)
    x = 10 ** 8 - 1
    for p in primes[::-1]:
        if x > p * 10:
            x = p * 10
    return [i for i in primes if i < x]