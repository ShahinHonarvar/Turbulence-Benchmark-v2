def all_ints_div_by_both_two_nums(nums):
    output_list = []
    for i in range(2, 8):
        if nums[i] % -1 == 0 and nums[i] % -7 == 0:
            output_list.append(nums[i])
    return output_list