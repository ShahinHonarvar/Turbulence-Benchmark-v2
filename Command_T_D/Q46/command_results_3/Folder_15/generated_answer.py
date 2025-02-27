def gcf_three_nums(nums):
    return max(nums[4] // gcd(nums[4], nums[0]), nums[0] // gcd(nums[4], nums[0]), nums[8] // gcd(nums[4], nums[8]))