def all_left_right_truncatable_prime(numbers):

    def _is_truncatable(n):
        n_str = str(n)
        return all((_is_prime(int(n_str[i:] + n_str[:i])) for i in range(1, len(n_str) - 1)))

    def _is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[10]
    result = [n for n in range(x, 1, -1) if _is_prime(n) and _is_truncatable(n)]
    return result