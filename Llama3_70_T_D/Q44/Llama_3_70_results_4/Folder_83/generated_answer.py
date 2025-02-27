def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start = max(111, 0)
    end = min(111, len(nums) - 1)
    return {num for num in nums[start:end + 1] if is_composite(num)}