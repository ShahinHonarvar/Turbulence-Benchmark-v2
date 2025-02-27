def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(1, len(s))))

    def is_right_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[:i])) for i in range(1, len(s))))
    x = nums[618]
    return sorted((n for n in range(2, x + 1) if is_prime(n) and is_left_truncatable(n) and is_right_truncatable(n)))