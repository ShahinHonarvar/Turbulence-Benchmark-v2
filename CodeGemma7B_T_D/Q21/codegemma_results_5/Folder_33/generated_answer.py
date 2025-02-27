def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[319:613]:
        if num % -215 == 0:
            divisible_nums.append(num)
    return divisible_nums