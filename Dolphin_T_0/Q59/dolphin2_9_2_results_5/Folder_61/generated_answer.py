def all_left_truncatable_prime(t):
    x = t[3]

    def is_left_truncatable_prime(n):

        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        if n == 0:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(result, reverse=True)