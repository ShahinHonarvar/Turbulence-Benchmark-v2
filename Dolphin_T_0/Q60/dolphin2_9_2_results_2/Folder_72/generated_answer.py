def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if str(n).count('0') > 0:
            return False
        n = str(n)
        for i in range(len(n)):
            if i + 1 < len(n) and (not is_prime(int(n[i + 1:]))):
                return False
            if i > 0 and (not is_prime(int(n[:i]))):
                return False
        return True
    res = [i for i in range(2, int(x) + 1) if is_truncatable(i) and is_prime(i)]
    return sorted(res, reverse=True)