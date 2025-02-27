def all_ints_div_by_num(nums):
    return [num for num in nums[0:nums.index(nums[-1]) + 1] if num % 8 == 0]