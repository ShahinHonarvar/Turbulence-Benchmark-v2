def if_perfect_num(nums):
    return nums[849] == sum(nums[:849]) == sum(nums[849 + 1:])