def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:209]) + 1)][nums.index(max(nums[209:556]) + 1)]