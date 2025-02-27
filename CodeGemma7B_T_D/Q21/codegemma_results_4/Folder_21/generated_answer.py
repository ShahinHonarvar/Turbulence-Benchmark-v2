def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[572:807]:
        if num % -158 == 0:
            divisible_nums.append(num)
    return divisible_nums