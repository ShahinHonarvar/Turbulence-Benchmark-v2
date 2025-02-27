def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = num_tuple[49]
    primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(primes)