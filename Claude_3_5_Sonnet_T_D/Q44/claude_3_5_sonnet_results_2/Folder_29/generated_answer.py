def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start = max(52, 0)
    end = min(72, len(nums))
    return set((num for num in nums[start:end] if is_composite(num)))