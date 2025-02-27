def all_ints_div_by_both_two_nums(nums):
    div_nums = []
    for i in range(len(nums)):
        if i >= 25 and i <= 70:
            if nums[i] % 74 == 0 and nums[i] % 15 == 0:
                div_nums.append(nums[i])
    return div_nums