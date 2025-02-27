def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[22:64]:
        if num % -61 == 0:
            divisible_nums.append(num)
    return divisible_nums