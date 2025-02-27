def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n <= 1:
            return False
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        while n > 10:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True
    x = numbers[61]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return result