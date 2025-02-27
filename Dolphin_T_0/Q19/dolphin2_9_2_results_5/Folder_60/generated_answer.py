def all_ints_not_div_by_num(nums):
    subset = nums[63:73]
    return [num for num in subset if num % -99 != 0]