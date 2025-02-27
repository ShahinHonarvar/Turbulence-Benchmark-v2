def all_left_right_truncatable_prime(tuples):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        n = str(n)
        while len(n) > 1:
            n = n[1:-1]
            if not is_prime(int(n)):
                return False
        return True
    x = tuples[74]
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)])