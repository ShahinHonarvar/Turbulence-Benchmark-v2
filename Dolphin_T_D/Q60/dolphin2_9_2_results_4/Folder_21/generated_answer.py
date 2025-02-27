def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, one):
        if len(n) == 1 or len(n) == 2:
            return is_prime(int(n))
        if n[0] == '0' or n[-1] == '0':
            return False
        return is_truncatable(n[1:], one) and is_truncatable(n[:-1], one)
    if len(numbers) < 175 or not isinstance(numbers, tuple):
        return []
    x = numbers[175]
    return sorted([int(i) for i in range(x + 1) if is_prime(i) and is_truncatable(str(i), True)])