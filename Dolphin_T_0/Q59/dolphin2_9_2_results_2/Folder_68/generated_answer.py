def all_left_truncatable_prime(x):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        while len(str_n) > 1:
            if is_prime(int(str_n)):
                str_n = str_n[1:]
            else:
                return False
        return True
    left_truncatables = [i for i in range(2, x) if is_truncatable(i) and is_prime(i)]
    left_truncatables.sort(reverse=True)
    return left_truncatables