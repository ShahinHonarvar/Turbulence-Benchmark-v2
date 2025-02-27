def find_second_largest_num(nums):
    if len(nums) <= 32:
        return 'None'
    nums.sort(reverse=True)
    if nums[32] == nums[33]:
        if len(nums) <= 35:
            return 'None'
        return nums[34]
    else:
        for i in range(32, 36):
            if nums[i] != nums[i + 1]:
                return nums[i + 1]