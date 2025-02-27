def all_ints_div_by_num(nums):
    if not nums:
        return []
    divisible_nums = []
    for i in range(421, 490):
        if nums[i] % 885 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums