def all_left_right_truncatable_prime(numbers):
    x = numbers[33]

    def is_left_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str) - 1):
            if n_str[i] == '0':
                return False
            if not is_prime(int(n_str[i + 1:])):
                return False
        return True

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return sorted((num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)))