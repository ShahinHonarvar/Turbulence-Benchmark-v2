def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    x = nums[30]
    return sorted([i for i in range(10, x) if left_truncatable(i) and is_prime(i)], reverse=True)