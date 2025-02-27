def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[31:51] if x % 81 == 0 or x % 64 == 0))