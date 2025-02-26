def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(nums) <= 57:
        return set()
    return {nums[i] for i in range(56, 58) if is_composite(nums[i])}