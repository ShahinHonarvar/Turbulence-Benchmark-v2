def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        num = n
        while num > 3:
            num = num % 10 ** (len(str(num)) - 1)
            if num == 0:
                return False
            if not is_prime(num):
                return False
        return True
    primes = []
    for i in range(10, x):
        if is_truncatable(i) and is_prime(i):
            primes.insert(0, i)
    return primes