def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[66:75]:
        if num % -14 == 0:
            divisible_nums.append(num)
    return divisible_nums