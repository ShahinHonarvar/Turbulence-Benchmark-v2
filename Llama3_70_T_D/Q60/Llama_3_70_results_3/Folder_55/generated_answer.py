def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        return '0' not in s and is_prime(n) and all((is_prime(int(s[i:-j or None])) for i in range(len(s)) for j in range(1, len(s) - i + 1)))
    x = numbers[73]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable(i)], reverse=True)