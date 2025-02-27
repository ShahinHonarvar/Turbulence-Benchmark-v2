def all_ints_not_div_by_num(nums):
    return [num for num in nums if num % 2 != 0 and 2 < nums.index(num) < len(nums) - 2]