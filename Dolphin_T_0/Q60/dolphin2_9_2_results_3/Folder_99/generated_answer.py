def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    primes = []
    for y in range(x, 10, -1):
        a = [int(i) for i in str(y)]
        trunc = [a[0]]
        while len(trunc) > 1:
            if int(''.join(map(str, trunc))) not in primes:
                if is_prime(int(''.join(map(str, trunc)))):
                    primes.append(int(''.join(map(str, trunc))))
                else:
                    break
            trunc = trunc[1:-1]
    return sorted(primes)