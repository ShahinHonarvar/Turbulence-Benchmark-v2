def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(args):
    x = args[39]
    primes = []
    for num in range(x - 1, 1, -1):
        while num >= 10 and is_prime(num):
            num = int(num / 10)
        if num == 1:
            primes.append(int(str(x - 1)[::-1]))
    return primes