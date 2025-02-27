def all_left_truncatable_prime(numbers):
    x = numbers[98]

    def check_prime(n):
        return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))

    def check_truncatable(n):
        while n > 0:
            if n % 10 == 0:
                return False
            if not check_prime(n):
                return False
            n //= 10
        return True
    return sorted([n for n in range(2, x) if check_truncatable(n)])