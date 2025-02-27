def sum_ints_div_by_either_nums(nums):
    if not nums:
        return 0
    return sum((num for num in nums[7:9] if num % 5 == 0 or num % 7 == 0))