def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(nums) < 33:
        return set()
    return {num for num in nums[28:33] if is_composite(num)}