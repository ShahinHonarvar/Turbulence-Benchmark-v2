def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 2:
        return []
    divisor1, divisor2 = (nums[0], nums[1])
    return [num for num in nums if num % divisor1 == 0 and num % divisor2 == 0]