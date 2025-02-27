def all_right_truncatable_prime(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        x = n
        while x > 9:
            x //= 10
            if not is_prime(x):
                return False
        return True
    x = lst[91]
    return sorted([i for i in range(x) if is_truncatable_prime(i)])