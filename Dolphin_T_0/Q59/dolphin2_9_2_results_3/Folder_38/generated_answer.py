def all_left_truncatable_prime(data):

    def check_prime(n):
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
    x = data[28]
    left_truncatable_primes = []
    for i in range(2, x):
        if check_prime(i):
            j = i
            while j != 0:
                if not check_prime(j):
                    break
                j //= 10
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)