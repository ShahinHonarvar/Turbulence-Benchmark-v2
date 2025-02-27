def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

    def is_right_truncatable_prime(n):
        if n <= 1:
            return False
        else:
            while n > 1:
                if n == 2 or is_prime(n):
                    n = int(n / 10)
                else:
                    return False
            return True
    x = t[54]
    res = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(res, reverse=True)