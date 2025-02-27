def all_ints_div_by_num(nums):
    divisible_nums = [num for num in nums[75:86] if num % -40 == 0]
    return divisible_nums if divisible_nums else []