def all_ints_div_by_num(nums):
    divisible_nums = [num for num in nums[29:52] if num % -37 == 0]
    return divisible_nums if divisible_nums else []