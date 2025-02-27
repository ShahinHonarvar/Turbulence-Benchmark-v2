def all_right_truncatable_prime(tupl):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        st = str(n)
        for i in range(1, len(st)):
            if not is_prime(int(st[i:])):
                return False
        return True
    x = tupl[61]
    truncatable = [i for i in range(2, x) if is_truncatable_prime(i)]
    return sorted(truncatable)