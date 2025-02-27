def all_left_right_truncatable_prime(args):
    x = args[10]

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

    def is_left_right_truncatable_prime(n):
        if is_prime(n):
            if not '0' in str(n):
                n = str(n)
                while len(n) > 2:
                    if not (is_prime(int(n[:-1])) and is_prime(int(n[1:]))):
                        return False
                    n = n[1:-1]
                return True
    return sorted([i for i in range(x, 0, -1) if is_left_right_truncatable_prime(i)], reverse=True)