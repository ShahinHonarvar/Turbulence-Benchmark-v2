def composite_nums_between_indices(nums):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {n for n in nums[21:98] if is_composite(n)}