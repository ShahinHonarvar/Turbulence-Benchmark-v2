def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str) - 1):
            if n_str[i] == '0' or not is_prime(int(n_str[i + 1:])) or (not is_prime(int(n_str[:i + 1]))):
                return False
        return True
    x = numbers[26]
    return sorted([i for i in range(x + 1) if is_left_right_truncatable_prime(i)])