def if_perfect_num(nums):
    return nums[87] == sum((1 if nums[87] % x == 0 else 0 for x in range(1, nums[87])))