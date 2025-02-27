def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[88]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            if len(primes) > 0 and primes[-1][-1] * 10 + i not in primes:
                break
            temp = [i]
            if all((is_prime(int(''.join(map(str, temp[i:])))) for i in range(len(temp)))):
                primes.extend(temp)
    return sorted(primes)