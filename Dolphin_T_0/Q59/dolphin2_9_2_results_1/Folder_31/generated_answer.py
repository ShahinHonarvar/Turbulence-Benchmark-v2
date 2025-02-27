def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        for i in range(len(s) - 1, -1, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = num_tuple[50]
    return sorted([n for n in range(x, 1, -1) if is_prime(n) and n % 10 != 0 and is_left_truncatable(n)])