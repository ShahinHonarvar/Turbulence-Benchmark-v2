def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[26]
    primes = []
    for i in range(2, x):
        if is_prime(i) and i > 9:
            max_digits = len(str(i))
            for j in range(1, max_digits):
                if is_prime(int(str(i)[-j:])):
                    i = int(str(i)[:-j])
                else:
                    break
            if i == 1:
                primes.append(int(str(i) + str(j)))
    primes.sort()
    return primes