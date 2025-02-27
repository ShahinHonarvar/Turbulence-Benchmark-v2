def all_left_right_truncatable_prime(input):

    def is_truncatable_prime(p):
        if '0' in str(p):
            return False
        while len(str(p)) > 1:
            p = int(str(p)[1:-1])
            if not is_prime(p):
                return False
        return True

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqr = int(n ** 0.5)
        for i in range(3, sqr + 1, 2):
            if n % i == 0:
                return False
        return True
    x = input[7]
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_truncatable_prime(i)])