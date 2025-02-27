def all_left_truncatable_prime(x):

    def is_left_truncatable_prime(n):
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp = temp // 10
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for n in reversed(range(2, x)):
        if is_left_truncatable_prime(n):
            primes.append(n)
    return primes