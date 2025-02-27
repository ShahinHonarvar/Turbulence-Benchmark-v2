def sum_ints_div_by_either_nums(nums):
    if not nums[13:19]:
        return 0
    return sum((number for number in nums[13:19] if number % 45 == 0 or number % 20 == 0))