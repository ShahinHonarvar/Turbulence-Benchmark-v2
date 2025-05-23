def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n == 0:
            return False
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[14]
    return [n for n in range(x - 1, 0, -1) if is_truncatable(n)]