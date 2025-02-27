def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        if len(str(n)) < 3:
            return is_prime(n)
        left = str(n)
        right = str(n)
        while len(left) > 2 and len(right) > 2:
            left = left[1:]
            right = right[:-1]
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
        return is_prime(int(left)) and is_prime(int(right))
    x = numbers[86]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)], reverse=True)