def composite_nums_between_indices(nums):

    def is_composite(n):
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((num for i, num in enumerate(nums[12:93], 12) if is_composite(num)))