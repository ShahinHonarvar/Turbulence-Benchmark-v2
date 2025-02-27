def all_left_right_truncatable_prime(numbers):
    x = numbers[81]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            left = int(str(n)[i:])
            right = int(str(n)[:-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)