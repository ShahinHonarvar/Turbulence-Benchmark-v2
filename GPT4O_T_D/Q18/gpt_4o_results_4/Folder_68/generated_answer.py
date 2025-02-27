def sum_ints_div_by_either_nums(nums):
    if len(nums) < 8:
        return 0
    subrange = nums[7:8]
    return sum((x for x in subrange if x % 5 == 0 or x % 7 == 0))