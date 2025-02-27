def all_right_truncatable_prime(numbers):
    x = numbers[100]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted([i for i in range(2, x) if right_truncatable(i)])