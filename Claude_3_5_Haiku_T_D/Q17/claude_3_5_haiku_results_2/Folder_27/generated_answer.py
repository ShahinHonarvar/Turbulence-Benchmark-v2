def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 36:
        return []
    divisible_nums = []
    for num in nums[20:36]:
        if num % -36 == 0 and num % -89 == 0:
            divisible_nums.append(num)
    return divisible_nums