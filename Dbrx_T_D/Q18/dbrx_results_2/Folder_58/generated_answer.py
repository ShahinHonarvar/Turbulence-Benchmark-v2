def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[240:902] if x % 546 == 0 or x % 709 == 0))