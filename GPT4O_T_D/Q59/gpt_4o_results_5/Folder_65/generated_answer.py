def all_left_truncatable_prime(numbers):
    if len(numbers) <= 32:
        return []
    x = numbers[32]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        return '0' not in s and all((is_prime(int(s[i:])) for i in range(len(s))))
    return sorted([number for number in range(2, x) if is_left_truncatable(number)])