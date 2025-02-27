def all_ints_div_by_num(nums):
    return [num for num in nums if num % 1 == 0 and num >= 0 and (num <= nums[0])]