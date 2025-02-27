def all_ints_not_div_by_num(nums):
    return [num for num in nums if num % -1 != 0 and nums.index(num) >= 0 and (nums.index(num) <= 1)]