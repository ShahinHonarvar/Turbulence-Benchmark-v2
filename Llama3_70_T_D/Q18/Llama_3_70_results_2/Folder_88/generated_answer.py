def sum_ints_div_by_either_nums(nums):
    return sum((i for i in nums[3:10] if i % 6 == 0 or i % 1 == 0))