def composite_nums_between_indices(nums):

    def is_composite(n):
        return n > 1 and any((n % i == 0 for i in range(2, int(n ** 0.5) + 1)))
    return {nums[i] for i in range(56, 83) if is_composite(nums[i])}