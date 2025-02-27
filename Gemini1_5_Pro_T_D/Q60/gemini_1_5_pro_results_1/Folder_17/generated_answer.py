def all_left_right_truncatable_prime(numbers):
    x = numbers[36]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n) or '0' in str(n):
            return False
        n_str = str(n)
        for i in range(len(n_str), 2, -1):
            if not is_prime(int(n_str[:i])):
                return False
            if not is_prime(int(n_str[i - 1:])):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result