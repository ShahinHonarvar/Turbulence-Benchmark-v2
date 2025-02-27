def all_left_truncatable_prime(numbers):

    def check_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[14]
    return sorted([i for i in range(2, x) if is_prime(i) and check_truncatable(i)], reverse=True)