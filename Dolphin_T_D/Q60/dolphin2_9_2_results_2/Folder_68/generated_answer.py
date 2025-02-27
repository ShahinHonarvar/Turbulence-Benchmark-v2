def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        i = 3
        w = int(n ** 0.5) + 1
        while i <= w:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(n):
        if n < 10:
            return True
        n = str(n)
        return is_prime(int(n[i + 1:])) and (is_prime(int(n[:i])) for i in range(len(n) - 1))
    return sorted([i for i in range(2, int(x) + 1) if is_truncatable(i)], reverse=True)