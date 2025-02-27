def all_left_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        while n and n[-1] == '0' and is_prime(int(n)):
            n = n[:-1]
        while n and n[0] == '0' and is_prime(int(n)):
            n = n[1:]
        return is_prime(int(n))
    x = int_tuple[79]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    return [p for p in primes if is_truncatable(p) and is_truncatable(p - 1)]