def gcf_three_nums(nums):
    return max(divmod(nums[693], nums[331])[1], divmod(nums[331], nums[668])[1], divmod(nums[668], nums[693])[1])