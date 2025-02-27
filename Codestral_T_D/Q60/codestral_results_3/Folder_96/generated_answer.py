def all_left_right_truncatable_prime(numbers):
    x = numbers[29]

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if not is_prime(n):
            return False
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)])