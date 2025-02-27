def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    x = nums[36]
    return sorted([n for n in range(2, x + 1) if is_prime(n) and is_left_right_truncatable(n)], reverse=True)