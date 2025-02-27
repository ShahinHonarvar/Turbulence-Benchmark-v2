def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[18]
    return [n for n in range(x - 1, 1, -1) if is_prime(n) and str(n).count('0') == 0 and all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))]