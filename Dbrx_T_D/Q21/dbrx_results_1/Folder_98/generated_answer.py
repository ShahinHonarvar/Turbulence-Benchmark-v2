def all_ints_div_by_num(nums):
    div_by_num = []
    for i in range(len(nums)):
        if nums[i] % 6 == 0:
            div_by_num.append(nums[i])
    return div_by_num