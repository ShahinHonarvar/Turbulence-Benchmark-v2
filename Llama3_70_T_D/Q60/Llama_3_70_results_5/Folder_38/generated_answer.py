def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        n_str = str(n)
        for _ in range(len(n_str) - 1):
            n_str = n_str[1:-1]
            if n_str and n_str[0] != '0' and (not is_prime(int(n_str))):
                return False
        return True
    x = numbers[28]
    return sorted([i for i in range(10, x + 1) if is_prime(i) and is_left_right_truncatable(i)])