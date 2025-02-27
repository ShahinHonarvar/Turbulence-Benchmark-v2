def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[61]
    primes = []
    for i in range(1, x + 1):
        if '0' in str(i):
            continue
        trunc = True
        for j in range(len(str(i)) - 1, 0, -1):
            if not is_prime(int(str(i)[j - 1]) + str(i)[j:]):
                trunc = False
                break
        if trunc:
            for j in range(1, len(str(i))):
                if not is_prime(str(i)[:j - 1] + str(i)[j] + str(i)[j + 1:]):
                    trunc = False
                    break
        if trunc:
            primes.append(i)
    return primes