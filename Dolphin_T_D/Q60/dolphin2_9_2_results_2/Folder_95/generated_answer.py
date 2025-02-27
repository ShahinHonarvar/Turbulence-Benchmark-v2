def all_left_right_truncatable_prime(n_tuple):

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

    def is_left_right_truncatable_prime(n):
        if n == 1:
            return False
        else:
            left_right_truncatable = True
            while n > 10:
                if n % 10 in (0, 1, 4, 5, 6, 9):
                    left_right_truncatable = False
                    break
                n //= 10
            return is_prime(n) and left_right_truncatable
    x = n_tuple[77]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatables = [i for i in primes if is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatables)