def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_and_right_truncatable(n):
        if n == 0 or n == 1:
            return False
        str_n = str(n)
        for i in range(len(str_n) - 1):
            if str_n[i] == '0':
                return False
            left = int(str_n[i + 1:])
            right = int(str_n[:i + 1])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    return sorted([i for i in range(x + 1) if is_left_and_right_truncatable(i)])