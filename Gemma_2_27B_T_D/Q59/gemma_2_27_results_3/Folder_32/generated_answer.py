def all_left_truncatable_prime(nums):
    x = nums[42]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    return sorted([num for num in range(2, x) if is_prime(num) and is_left_truncatable(num)])