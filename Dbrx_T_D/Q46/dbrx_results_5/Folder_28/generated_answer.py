def gcf_three_nums(nums):
    if not all((isinstance(i, int) and i > 0 for i in nums)):
        raise ValueError('All list elements must be positive integers')

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(nums[99], nums[63]), nums[74])