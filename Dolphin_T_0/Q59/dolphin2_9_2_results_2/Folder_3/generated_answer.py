def all_left_truncatable_prime(t):

    def is_left_truncatable_prime(n):
        if all((int(d) != 0 for d in str(n))):
            trunc = n
            while trunc > 1:
                if not is_prime(trunc):
                    return False
                trunc //= 10
            return True
        return False

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[100]
    return [n for n in range(2, x) if is_left_truncatable_prime(n)]