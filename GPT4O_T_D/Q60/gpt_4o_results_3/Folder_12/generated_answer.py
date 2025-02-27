def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(p):
        if '0' in str(p):
            return False
        n = len(str(p))
        return all((is_prime(int(str(p)[i:n - i])) for i in range((n - 1) // 2 + 1)))
    x = numbers[70]
    result = [num for num in range(2, x + 1) if is_prime(num) and is_left_right_truncatable(num)]
    return sorted(result, reverse=True)