def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[86]
    primes = [2, 3]
    for num in range(10, x + 1):
        if all([int(str(num)[i]) != 0 and is_prime(int(str(num)[i + 1:j + 1])) for i, j in zip(range(len(str(num))), range(1, len(str(num))))]):
            primes.append(num)
    if not primes:
        return []
    primes.sort()
    return primes