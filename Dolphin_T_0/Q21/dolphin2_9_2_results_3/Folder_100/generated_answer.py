def all_ints_div_by_num(nums):
    output = []
    for i in range(86, 93):
        if i in nums and nums[i] % 86 == 0:
            output.append(nums[i])
    return output