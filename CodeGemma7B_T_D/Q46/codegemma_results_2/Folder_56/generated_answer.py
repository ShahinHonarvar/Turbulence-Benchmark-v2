def gcf_three_nums(nums):
    """Return the greatest common factor of the elements at indices 59, 93, and 84."""
    min_num = min([nums[59], nums[93], nums[84]])
    while min_num > 1:
        for i in range(min_num, 0, -1):
            if nums[59] % i == 0 and nums[93] % i == 0 and (nums[84] % i == 0):
                min_num = i
                break
    return min_num