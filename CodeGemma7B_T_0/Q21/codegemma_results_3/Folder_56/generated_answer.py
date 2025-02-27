def all_ints_div_by_num(nums):
    return [num for num in nums if num % 6 == 0 and num in range(nums[0], nums[-1] + 1)]