def all_ints_div_by_num(nums):
    return [n for n in nums if n % 5 == 0 and n in range(nums[0], nums[-1] + 1)]