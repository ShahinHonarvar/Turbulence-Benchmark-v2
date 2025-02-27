def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    composite_nums = set()
    if 2 < len(nums) < 3:
        for i in range(2, min(3, len(nums))):
            if is_composite(nums[i]):
                composite_nums.add(nums[i])
    return composite_nums