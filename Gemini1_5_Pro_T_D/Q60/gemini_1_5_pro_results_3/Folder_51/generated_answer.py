def all_left_right_truncatable_prime(numbers):
    x = numbers[54]

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
        left = str(n)[1:]
        right = str(n)[::-1][1:][::-1]
        while len(left) > 0 and len(right) > 0:
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
            left = left[1:]
            right = right[::-1][1:][::-1]
        return True
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return result