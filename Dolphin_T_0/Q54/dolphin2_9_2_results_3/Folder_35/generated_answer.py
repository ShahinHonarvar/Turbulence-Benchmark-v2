def all_right_truncatable_prime(tuple_of_integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if not is_prime(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = tuple_of_integers[177]
    primes = []
    i = 2
    while i < x:
        if is_truncatable(i):
            primes.append(i)
        i += 1
    return sorted(primes)