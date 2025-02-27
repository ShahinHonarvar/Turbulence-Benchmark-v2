def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:i])):
                return False
        return True
    x = nums[52]
    return sorted([i for i in range(2, x + 1) if '0' not in str(i) and is_left_right_truncatable_prime(i)], reverse=True)