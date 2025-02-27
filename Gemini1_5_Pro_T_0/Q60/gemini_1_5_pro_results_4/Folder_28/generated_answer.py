def all_left_right_truncatable_prime(numbers):
    x = numbers[19]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n <= 1 or '0' in str(n):
            return False
        if not is_prime(n):
            return False
        left_truncations = [str(n)[i:] for i in range(len(str(n)))]
        right_truncations = [str(n)[:i] for i in range(1, len(str(n)))]
        for num in left_truncations + right_truncations:
            if not is_prime(int(num)):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return result