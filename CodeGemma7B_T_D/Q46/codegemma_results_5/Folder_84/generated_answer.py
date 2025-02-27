def gcf_three_nums(nums):
    max_value = max(nums[695], nums[710], nums[914])
    factor = max_value
    while factor > 0:
        if nums[695] % factor == 0 and nums[710] % factor == 0 and (nums[914] % factor == 0):
            return factor
        factor -= 1