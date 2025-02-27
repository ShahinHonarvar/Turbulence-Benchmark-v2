def all_left_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[25]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and (not '0' in str(i)):
            for j in range(len(str(i)) - 1):
                if not is_prime(int(str(i)[j + 1:])):
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)