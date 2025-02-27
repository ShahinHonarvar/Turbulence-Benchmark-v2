def all_left_right_truncatable_prime(numbers):
    x = numbers[96]

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(n):
        if all((is_prime(int(str(n)[-i - 1:-i])) and is_prime(int(str(n)[i:i + 2])) for i in range(1, len(str(n)) - 1))):
            return is_prime(int(str(n)[-2:])) and is_prime(int(str(n)[:2]))
        return False
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)], reverse=True)