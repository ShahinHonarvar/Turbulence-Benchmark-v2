def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        if num < 10 or '0' in str(num):
            return False
        left = str(num)
        right = str(num)
        while len(left) > 1 or len(right) > 1:
            if len(left) > 1:
                left = left[1:]
                if not is_prime(int(left)):
                    return False
            if len(right) > 1:
                right = right[:-1]
                if not is_prime(int(right)):
                    return False
        return True
    x = numbers[89]
    left_right_truncatable_primes = [num for num in range(x, 1, -1) if is_left_right_truncatable_prime(num)]
    return left_right_truncatable_primes