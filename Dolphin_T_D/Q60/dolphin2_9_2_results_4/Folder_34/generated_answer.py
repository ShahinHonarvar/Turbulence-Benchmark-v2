def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if n // 10 == 0:
            return True
        m = n
        while m // 10 != 0:
            m //= 10
        while m >= 10:
            m //= 10
        return m in (2, 3, 5, 7)

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = numbers[18]
    return sorted([n for n in range(1, x + 1) if is_prime(n) and is_truncatable_prime(n)], reverse=True)