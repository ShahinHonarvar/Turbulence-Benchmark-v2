def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[42]
    primes = []
    for i in range(1, x):
        if is_prime(i):
            if len(primes) == 0:
                primes.append(i)
            else:
                digit = primes[-1]
                while digit:
                    if i // digit == primes[-1]:
                        primes.append(i)
                        break
                    digit //= 10
    return sorted(primes)