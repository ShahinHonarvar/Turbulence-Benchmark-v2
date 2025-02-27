def all_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def is_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str) - 1, 0, -1):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    return sorted([i for i in range(2, x) if is_prime(i) and is_truncatable(i)], reverse=True)