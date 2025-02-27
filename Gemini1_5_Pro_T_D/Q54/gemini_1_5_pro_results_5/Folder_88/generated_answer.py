def all_right_truncatable_prime(numbers):
    x = numbers[93]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(len(str(n))):
            if not all((n % j for j in range(2, int(n ** 0.5) + 1))):
                return False
            n //= 10
        return True
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])