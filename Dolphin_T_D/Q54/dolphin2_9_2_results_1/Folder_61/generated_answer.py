def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if is_prime(n):
        str_n = str(n)
        for i in range(len(str_n) - 1, 0, -1):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    return False

def all_right_truncatable_prime(args):
    x = args[3]
    primes = []
    for i in range(x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)