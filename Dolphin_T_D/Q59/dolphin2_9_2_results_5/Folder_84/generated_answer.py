def all_left_truncatable_prime(tuple_of_ints):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_trun(n):
        while n > 1 and n % 10:
            if not is_prime(n):
                return False
            n //= 10
        return n == 1
    x = tuple_of_ints[630]
    primes_left_trun = [i for i in range(x - 1, 1, -1) if left_trun(i) and is_prime(i)]
    return primes_left_trun