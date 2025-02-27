def all_ints_div_by_num(nums):
    for i in range(10, 38):
        if nums[i] % -64 == 0:
            return nums[i]
    return []