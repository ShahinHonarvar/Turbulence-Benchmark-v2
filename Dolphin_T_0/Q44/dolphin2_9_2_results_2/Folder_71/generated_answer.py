def composite_nums_between_indices(nums):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((nums[i] for i in range(59, 98) if is_composite(nums[i])))