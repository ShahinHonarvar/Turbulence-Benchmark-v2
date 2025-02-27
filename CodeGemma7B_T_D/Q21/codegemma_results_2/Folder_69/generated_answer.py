def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[43:77]:
        if num % 14 == 0:
            divisible_nums.append(num)
    if not divisible_nums:
        return []
    return divisible_nums