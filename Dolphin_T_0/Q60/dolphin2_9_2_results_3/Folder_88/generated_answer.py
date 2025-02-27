def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable(n):
        while len(str(n)) > 2:
            n = int(str(n)[1:-1])
            if str(n).count('0') > 0 or not is_prime(n):
                return False
        return True
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_lr_truncatable(i):
            primes.append(i)
    return sorted(primes)