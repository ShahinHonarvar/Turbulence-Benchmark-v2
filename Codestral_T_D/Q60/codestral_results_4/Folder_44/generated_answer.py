def all_left_right_truncatable_prime(numbers):
    x = numbers[39]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n %= 10 ** (len(str(n)) - 1)
        return True
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)