def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[14]

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

    def is_truncatable_prime(n):
        while n > 10:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return is_prime(n)
    result = [i for i in range(1, x + 1) if is_truncatable_prime(i)]
    return sorted(result, reverse=True)