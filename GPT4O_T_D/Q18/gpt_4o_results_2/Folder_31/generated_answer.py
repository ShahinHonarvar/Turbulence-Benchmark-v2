def sum_ints_div_by_either_nums(nums):
    if len(nums) < 89:
        return 0
    return sum((num for num in nums[56:89] if num % -59 == 0 or num % -79 == 0))