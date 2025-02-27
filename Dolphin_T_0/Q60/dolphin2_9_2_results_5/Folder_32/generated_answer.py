def all_left_right_truncatable_prime(numbers):

    def is_prime(y):
        if y < 2:
            return False
        for i in range(2, int(y ** 0.5) + 1):
            if y % i == 0:
                return False
        return True

    def is_left_right_truncatable(y):
        while y > 9:
            y1 = y // 10
            y2 = y % 10
            if not is_prime(y1) or not is_prime(y2):
                return False
            y = y1
        return True
    x = numbers[42]
    return sorted([y for y in range(2, x + 1) if is_prime(y) and is_left_right_truncatable(y)])