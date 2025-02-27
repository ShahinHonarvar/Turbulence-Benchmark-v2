def all_ints_div_by_num(nums):
    new_nums = []
    for num in nums[5:7]:
        if num % 6 == 0:
            new_nums.append(num)
    return new_nums