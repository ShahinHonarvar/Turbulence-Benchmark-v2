def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str), 0, -1):
            if not is_prime(int(n_str[:i])):
                return False
        return True
    x = numbers[26]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])