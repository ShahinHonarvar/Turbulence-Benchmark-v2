def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True
    x = t[46]
    primes = []
    for i in range(1, x):
        if is_prime(i) and (not '0' in str(i)):
            if all([is_prime(int(str(i)[+1:])) for i in range(len(str(i)) - 1)]) and all([int(str(i)[k]) != 0 for k in range(len(str(i)) - 1)]):
                primes.append(i)
    return sorted(primes, reverse=True)