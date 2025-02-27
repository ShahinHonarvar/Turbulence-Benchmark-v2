def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        for _ in range(len(str_n) - 1):
            str_n = str_n[1:-1]
            if not str_n or not is_prime(int(str_n)):
                return False
        return True
    x = numbers[39]
    return sorted([i for i in range(2, x + 1) if '0' not in str(i) and is_prime(i) and is_left_right_truncatable_prime(i)])