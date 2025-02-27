def all_left_right_truncatable_prime(numbers):
    x = numbers[24]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        if n < 10:
            return True
        n_str = str(n)
        for i in range(1, len(n_str)):
            left_trunc = int(n_str[i:])
            right_trunc = int(n_str[:-i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return True
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return result