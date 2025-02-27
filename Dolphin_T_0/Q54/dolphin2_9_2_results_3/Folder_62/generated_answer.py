def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[70]
    primes = [2, 3, 5, 7]
    current = 2
    while current < x:
        if is_prime(current):
            trunc = current
            while len(str(trunc)) > 1 and is_prime(int(str(trunc)[-1])):
                trunc = int(str(trunc)[-1])
                if trunc not in primes:
                    primes.append(trunc)
        current += 1
    return primes