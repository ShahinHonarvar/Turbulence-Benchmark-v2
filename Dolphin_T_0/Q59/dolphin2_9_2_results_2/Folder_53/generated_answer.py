def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[86]
    primes = [2, 3, 5, 7]
    i = 10
    while primes[-1] < x:
        if all((is_prime(int(str(i)[j:])) for j in range(len(str(i))))):
            primes.append(i)
        i += 1
    return primes[::-1]