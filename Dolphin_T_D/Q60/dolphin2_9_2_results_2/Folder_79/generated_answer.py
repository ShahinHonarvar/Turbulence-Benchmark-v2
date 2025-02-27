def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable_prime(n):
        if n == 0:
            return False
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return is_prime(n)
    return [i for i in range(x + 1) if left_right_truncatable_prime(i)]