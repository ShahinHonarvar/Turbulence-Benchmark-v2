def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[46]
    return sorted([n for n in reversed(range(x)) if is_right_truncatable(n)], reverse=False)