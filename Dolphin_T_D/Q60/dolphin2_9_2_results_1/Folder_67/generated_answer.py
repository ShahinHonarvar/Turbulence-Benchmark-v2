def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, i):
        if i == 0:
            return is_prime(n)
        return is_truncatable_prime(n // 10, i - 1) and is_prune(n % 10 ** i, i - 1)
    primer = [i for i in range(2, x + 1) if is_prime(i)]
    ret = [i for i in primer if is_truncatable_prime(i, len(str(i)) - 1)]
    return sorted(ret, reverse=True)