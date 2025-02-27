def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n == 1:
            return True
        elif n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_truncatable_prime(int(str(n)[1:-1]))
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    return [i for i in primes if is_truncatable_prime(i)][::-1]