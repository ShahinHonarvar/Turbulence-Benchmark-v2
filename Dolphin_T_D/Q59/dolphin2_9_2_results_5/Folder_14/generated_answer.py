def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if any((int(digit) == 0 for digit in str(n))):
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[78]
    return sorted([n for n in range(2, x) if is_left_truncatable(n)], reverse=True)