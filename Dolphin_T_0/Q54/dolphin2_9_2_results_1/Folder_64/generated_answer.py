def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        while n > 0:
            if n < 2 or not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[4]
    return sorted((x for x in range(2, x) if right_truncatable_prime(x)))