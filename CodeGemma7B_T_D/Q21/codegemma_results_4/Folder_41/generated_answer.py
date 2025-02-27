def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[0:6]:
        if num % 5 == 0:
            divisible_nums.append(num)
    return divisible_nums