def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, round(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if str(n).count('0') > 0:
            return False
        while len(str(n)) != 1 and len(str(n)) != 2:
            if not is_prime(n // 10) or not is_prime(n % 10 ** len(str(n)) // 10):
                return False
            n //= 10
        return True
    x = numbers[758 - 1]
    result = [i for i in range(x + 1) if is_truncatable(i)]
    return result