def all_left_right_truncatable_prime(numbers):
    x = numbers[4]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n) or '0' in str(n):
            return False
        left = str(n)
        right = str(n)
        while len(left) > 1:
            left = left[1:]
            right = right[:-1]
            if not (is_prime(int(left)) and is_prime(int(right))):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return result