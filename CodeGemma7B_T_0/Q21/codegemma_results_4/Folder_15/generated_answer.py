def all_ints_div_by_num(nums):
    return [num for num in nums if num % 3 == 0 and num >= 0 and (num <= nums[0])]